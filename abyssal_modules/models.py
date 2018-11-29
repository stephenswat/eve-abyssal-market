from django.db import models
from django.utils import timezone
from django.db.models import OuterRef, Subquery, F, Value, Case, When, Window
from django.db.models import ExpressionWrapper, BigIntegerField, DecimalField
from django.db.models.functions import Cast, PercentRank
from django.utils.functional import cached_property

from eve_esi import ESI
from eve_sde.models import InvType


DERIVED_ATTRIBUTES = {
    100000: {
        'types': [47781, 47785, 47789, 47793, 47836, 47838, 47840],
        'name': 'Shield boost per second',
        'unit_str': 'HP/s',
        'value': lambda x: x.get_value(68) / x.get_value(73),
        'high_is_good': True
    },
    100001: {
        'types': [47769, 47773, 47777, 47842, 47844, 47846],
        'name': 'Armor repair per second',
        'unit_str': 'HP/s',
        'value': lambda x: x.get_value(84) / x.get_value(73),
        'high_is_good': True
    },
    100002: {
        'types': [47781, 47785, 47789, 47793],
        'name': 'Shield boost per capacitor',
        'unit_str': 'HP/GJ',
        'value': lambda x: x.get_value(68) / x.get_value(6),
        'high_is_good': True
    },
    100003: {
        'types': [47769, 47773, 47777, 47842, 47844, 47846],
        'name': 'Armor repair per capacitor',
        'unit_str': 'HP/GJ',
        'value': lambda x: x.get_value(84) / x.get_value(6),
        'high_is_good': True
    },
    100004: {
        'types': [49730, 49722, 49726, 49734],
        'name': 'DPS Bonus',
        'unit_str': '%',
        'value': lambda x: ((x.get_value(64) * 1 / (1 - x.get_value(204) / 100)) - 1) * 100,
        'high_is_good': True
    },
    100005: {
        'types': [49738],
        'name': 'DPS Bonus',
        'unit_str': '%',
        'value': lambda x: (((x.get_value(213) / 100 + 1) / (1 - (x.get_value(204) / 100))) - 1) * 100,
        'high_is_good': True
    },
}


class EveCharacterManager(models.Manager):
    def get_or_create_by_id(self, character_id):
        try:
            return self.model.objects.get(id=character_id)
        except self.model.DoesNotExist:
            character_data = ESI.request(
                'get_characters_character_id',
                character_id=character_id
            ).data

            character, _ = EveCharacter.objects.update_or_create(
                id=character_id,
                defaults={
                    'name': character_data['name']
                }
            )

            return character


class EveCharacter(models.Model):
    objects = EveCharacterManager()

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class ModuleDogmaAttribute(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=64)

    unit_str = models.CharField(max_length=16)

    is_derived = models.BooleanField(default=False)

    @property
    def icon_path(self):
        return "/img/attributes/%d.png" % self.id

    @property
    def derived(self):
        return getattr(self, '_derived', False)

    def __str__(self):
        return self.name


class ModuleType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)

    attributes = models.ManyToManyField(
        ModuleDogmaAttribute,
        through='TypeAttribute',
        related_name='+'
    )

    @property
    def attribute_list(self):
        attrs = list(
            self.attributes
            .filter(typeattribute__display=True)
            .annotate(high_is_good=F("typeattribute__high_is_good"))
            .order_by('id')
            .all()
        )

        for attr_id, data in DERIVED_ATTRIBUTES.items():
            if self.id not in data['types']:
                continue

            new_attr = ModuleDogmaAttribute(
                id=attr_id,
                name=data['name'],
                unit_str=data['unit_str']
            )

            new_attr._derived = True
            new_attr.high_is_good = data['high_is_good']

            attrs.append(new_attr)

        return attrs

    def __str__(self):
        return self.name


class ModuleManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .prefetch_related(
                'source',
                'mutator',
                'moduleattribute_set__attribute',
                'moduleattribute_set',
                'type',
            )
        )


class AvailableModuleManager(ModuleManager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .filter(
                contracts__available=True,
                contracts__expires_at__gte=timezone.now()
            )
            .annotate(
                contract_price=F('contracts__price'),
                contract_plex=F('contracts__plex'),
                contract_price_inc_plex=ExpressionWrapper(
                    Cast('contracts__plex', BigIntegerField()) *
                    Value(3300000, output_field=BigIntegerField()) +
                    F('contracts__price'),
                    output_field=DecimalField()
                ),
                contract_id=F('contracts__id'),
                contract_single=F('contracts__single_item'),
                contract_auction=F('contracts__auction')
            )
        )


class Module(models.Model):
    objects = ModuleManager()
    available = AvailableModuleManager()

    id = models.BigIntegerField(primary_key=True)
    type = models.ForeignKey(
        ModuleType,
        models.CASCADE,
        related_name='modules',
        db_index=True
    )

    mutator = models.ForeignKey(
        InvType,
        models.CASCADE,
        related_name='+',
    )
    source = models.ForeignKey(
        InvType,
        models.CASCADE,
        related_name='+',
    )

    creator = models.ForeignKey(
        EveCharacter,
        models.CASCADE,
        related_name='creations'
    )

    attributes = models.ManyToManyField(
        ModuleDogmaAttribute,
        through='ModuleAttribute',
        related_name='+'
    )

    first_seen = models.DateTimeField(auto_now_add=True, db_index=True)

    def attribute_dict_with_derived(self):
        res = {
            x.attribute.id: {
                'real_value': x.real_value,
                'rating': int(round(x.rating)),
                'unit': x.attribute.unit_str
            }
            for x in self.moduleattribute_set.all() if x.display
        }

        if self.type_id == 49738 and 1255 not in res:
            res[1255] = {
                'real_value': 0.0,
                'rating': None,
                'unit': '%'
            }

        for attr_id, data in DERIVED_ATTRIBUTES.items():
            if self.type_id not in data['types']:
                continue

            res[attr_id] = {
                'real_value': data['value'](self),
                'rating': None,
                'unit': data['unit_str']
            }

        return res

    @cached_property
    def attribute_list(self):
        return sorted(self.attribute_dict.values(), key=lambda x: x.attribute.id)

    @cached_property
    def attribute_dict(self):
        return {
            x.attribute.id: x
            for x in self.moduleattribute_set.all() if x.display
        }

    def get_value(self, attr_id):
        if attr_id in DERIVED_ATTRIBUTES:
            return DERIVED_ATTRIBUTES[attr_id]['value'](self)

        attrs = self.attribute_dict

        if attr_id == 1255 and self.type.id == 49738 and attr_id not in attrs:
            return 0.0
        elif attr_id not in attrs:
            raise ValueError("Object does not have an attribute %d." % attr_id)
        else:
            return attrs[attr_id].real_value

    def get_pyfa_string(self):
        attr_list = ", ".join(
            "{attr_name} {attr_value:0.3f}".format(
                attr_name=a.attribute.short_name,
                attr_value=a.value
            )
            for a in self.attribute_list
        )

        return (
            "{module_type}\n" +
            "  {mutator_name}\n" +
            "  {attr_list}"
        ).format(
            module_type=self.source.name,
            mutator_name=self.mutator.name,
            attr_list=attr_list
        )

    def as_dict(self):
        return {
            'id': self.id,
            'type_id': self.type.id,
            'type_name': self.type.name,
            'attributes': self.attribute_dict_with_derived(),
            'contract': {
                'id': self.contract_id,
                'price': {
                    'isk': self.contract_price,
                    'plex': self.contract_plex,
                    'total': self.contract_price_inc_plex
                },
                'auction': self.contract_auction,
                'multi_item': not self.contract_single
            },
            'pyfa': self.get_pyfa_string()
        }


class ModuleAttributeManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .annotate(
                display=Subquery(
                    TypeAttribute.objects
                    .filter(
                        type=OuterRef('module__type'),
                        attribute=OuterRef('attribute')
                    )
                    .values('display')[:1]
                ),
                real_value=Case(
                    When(attribute_id__in=[73, 1795], then=F('value') * Value(0.001)),
                    When(attribute_id__in=[147], then=F('value') * Value(100)),
                    When(attribute_id__in=[213], then=(F('value') - Value(1)) * Value(100)),
                    When(attribute_id__in=[204], then=(Value(1) - F('value')) * Value(100)),
                    default=F('value')
                )
            )
            .annotate(
                high_is_good=Subquery(
                    TypeAttribute.objects
                    .filter(
                        type=OuterRef('module__type'),
                        attribute=OuterRef('attribute')
                    )
                    .values('high_is_good')
                )
            )
            .annotate(
                rating=(
                    (Window(
                        expression=PercentRank(),
                        partition_by=[F('attribute_id'), F('module__type_id')],
                        order_by=F('real_value').asc()
                    ) * Value(10) - Value(5)) *
                    Case(
                        When(high_is_good=True, then=Value(1)),
                        default=Value(-1)
                    )
                )
            )
        )


class ModuleAttribute(models.Model):
    module = models.ForeignKey(Module, models.CASCADE)
    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)

    value = models.FloatField(db_index=True)

    objects = ModuleAttributeManager()


class TypeAttribute(models.Model):
    type = models.ForeignKey(ModuleType, models.CASCADE)
    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)

    display = models.BooleanField(default=False)
    high_is_good = models.NullBooleanField()


class Mutator(models.Model):
    item_type = models.OneToOneField(InvType, models.CASCADE, related_name='+')
    result = models.ForeignKey(ModuleType, models.CASCADE)

    applicable_modules = models.ManyToManyField(InvType)
    attributes = models.ManyToManyField(TypeAttribute, through='MutatorAttribute')


class MutatorAttribute(models.Model):
    mutator = models.ForeignKey(Mutator, models.CASCADE)
    attribute = models.ForeignKey(TypeAttribute, models.CASCADE)

    min_modifier = models.DecimalField(max_digits=10, decimal_places=5)
    max_modifier = models.DecimalField(max_digits=10, decimal_places=5)
