from django.db import models
from django.utils import timezone
from django.db.models import F, Value, Case, When, FloatField
from django.db.models import ExpressionWrapper, BigIntegerField, DecimalField
from django.db.models.functions import Cast
from django.utils.functional import cached_property

from eve_esi import ESI
from eve_sde.models import InvType


DERIVED_ATTRIBUTES = {
    100000: {
        'types': [47781, 47785, 47789, 47793, 47836, 47838, 47840],
        'name': 'Shield boost per second',
        'unit_str': 'HP/s',
        'value': lambda x: x.get_value(68) / x.get_value(10073),
        'high_is_good': True
    },
    100001: {
        'types': [47769, 47773, 47777, 47842, 47844, 47846],
        'name': 'Armor repair per second',
        'unit_str': 'HP/s',
        'value': lambda x: x.get_value(84) / x.get_value(10073),
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
        'value': lambda x: ((x.get_value(64) * 1 / (1 - x.get_value(10204) / 100)) - 1) * 100,
        'high_is_good': True
    },
    100005: {
        'types': [49738],
        'name': 'DPS Bonus',
        'unit_str': '%',
        'value': lambda x: (((x.get_value(10213) / 100 + 1) / (1 - (x.get_value(10204) / 100))) - 1) * 100,
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
                'attribute_values',
                'attribute_values__attribute',
                'attribute_values__new_attribute',
                'attribute_values__new_attribute__type',
                'attribute_values__new_attribute__attribute',
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


class ModuleBase(models.Model):
    id = models.BigIntegerField(primary_key=True)

    attributes = models.ManyToManyField(
        ModuleDogmaAttribute,
        through='ModuleAttribute',
        related_name='+'
    )

    source = models.ForeignKey(
        InvType,
        models.CASCADE,
        related_name='+',
    )

    class Meta:
        abstract = True

    def attribute_dict(self):
        res = {
            x.attribute.id: {
                'real_value': x.value,
                'rating': int(round(x.rating)) if x.rating is not None and not self._is_static else None,
                'unit': x.attribute.unit_str,
                'display': x.new_attribute.display
            }
            for x in self.attribute_values.all()
        }

        if self.type_id == 49738 and 1255 not in res:
            res[1255] = {
                'real_value': 0.0,
                'rating': None,
                'unit': '%',
                'display': True
            }

        for attr_id, data in DERIVED_ATTRIBUTES.items():
            if self.type_id not in data['types']:
                continue

            res[attr_id] = {
                'real_value': data['value'](self),
                'rating': None,
                'unit': data['unit_str'],
                'display': True
            }

        return res

    @cached_property
    def attribute_list(self):
        return sorted(self.attribute_values.all(), key=lambda x: x.attribute.id)

    def get_value(self, attr_id):
        if attr_id in DERIVED_ATTRIBUTES:
            return DERIVED_ATTRIBUTES[attr_id]['value'](self)

        attrs = {x.attribute.id: x for x in self.attribute_values.all()}

        if attr_id == 1255 and self.type.id == 49738 and attr_id not in attrs:
            return 0.0
        elif attr_id not in attrs:
            raise ValueError("Object does not have an attribute %d." % attr_id)
        else:
            return attrs[attr_id].value

    def as_dict(self):
        return {
            'id': self.id,
            'type_id': self.type.id,
            'type_name': self.type.name,
            'attributes': self.attribute_dict()
        }


class StaticModuleManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .prefetch_related(
                'source',
                'attribute_values__attribute',
                'attribute_values',
                'type',
            )
        )


class StaticModule(ModuleBase):
    type = models.ForeignKey(
        ModuleType,
        models.CASCADE,
        related_name='static_modules',
        db_index=True
    )

    objects = StaticModuleManager()

    @property
    def _is_static(self):
        return True

    def as_dict(self):
        return {
            **super().as_dict(),
            'contract': None,
            'pyfa': None,
            'static': True,
            'module_name': self.source.name
        }


class Module(ModuleBase):
    objects = ModuleManager()
    available = AvailableModuleManager()

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

    creator = models.ForeignKey(
        EveCharacter,
        models.CASCADE,
        related_name='creations'
    )

    first_seen = models.DateTimeField(auto_now_add=True, db_index=True)

    @property
    def _is_static(self):
        return False

    def get_pyfa_string(self):
        attr_list = ", ".join(
            "{attr_name} {attr_value:f}".format(
                attr_name=a.attribute.short_name,
                attr_value=a.value
            )
            for a in self.attribute_values.all()
            if a.new_attribute.pyfa_display
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
        res = {
            **super().as_dict(),
            'pyfa': self.get_pyfa_string(),
            'static': False
        }

        if hasattr(self, 'contract_id'):
            res['contract'] = {
                'id': self.contract_id,
                'price': {
                    'isk': self.contract_price,
                    'plex': self.contract_plex,
                    'total': self.contract_price_inc_plex
                },
                'auction': self.contract_auction,
                'multi_item': not self.contract_single
            }

        return res


class UnratedModuleAttributeManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .prefetch_related(
                'new_attribute',
                'new_attribute__type',
                'new_attribute__attribute',
                'attribute',
                'module',
                'static_module'
            )
        )


class ModuleAttributeManager(UnratedModuleAttributeManager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .annotate(
                rating=(
                    Case(
                        When(new_attribute__aggregates__stddev=0, then=Value(0, output_field=FloatField())),
                        default=(
                            F('value') - F('new_attribute__aggregates__avg')
                        ) / F('new_attribute__aggregates__stddev')
                    ) * Value(4) * Case(
                        When(new_attribute__high_is_good=True, then=Value(1)),
                        default=Value(-1)
                    )
                )
            )
        )


class ModuleAttributeAggregate(models.Model):
    new_attribute = models.OneToOneField(
        'TypeAttribute', models.DO_NOTHING, primary_key=True, related_name='aggregates'
    )

    avg = models.FloatField()
    stddev = models.FloatField()

    class Meta:
        managed = False
        db_table = 'abyssal_modules_attribute_stats__view'


class ModuleAttributeView(models.Model):
    module = models.ForeignKey(Module, models.CASCADE, null=True, related_name='attribute_values')
    static_module = models.ForeignKey(StaticModule, models.CASCADE, null=True, related_name='attribute_values')

    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)
    new_attribute = models.ForeignKey('TypeAttribute', models.CASCADE)

    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'abyssal_modules_derived_attributes__view'

    objects = ModuleAttributeManager()
    unrated = UnratedModuleAttributeManager()

    def rounded_rating(self):
        return int(round(self.rating))


class ModuleAttribute(models.Model):
    module = models.ForeignKey(Module, models.CASCADE, null=True)
    static_module = models.ForeignKey(StaticModule, models.CASCADE, null=True)

    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)
    new_attribute = models.ForeignKey('TypeAttribute', models.CASCADE)

    value = models.FloatField(db_index=True)


class TypeAttribute(models.Model):
    type = models.ForeignKey(ModuleType, models.CASCADE)
    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)

    display = models.BooleanField(default=False)
    high_is_good = models.NullBooleanField()

    @property
    def pyfa_display(self):
        return self.attribute_id in {
            1795, 6, 1159, 20, 796, 30, 554, 50, 54, 64, 67, 68, 72, 73, 204,
            84, 213, 983, 90, 2267, 97
        }


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
