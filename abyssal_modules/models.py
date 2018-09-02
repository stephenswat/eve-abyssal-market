from django.db import models
from django.utils import timezone
from django.db import transaction
from django.db.models import OuterRef, Subquery, F

from eve_esi import ESI
from contract_scanner.models import Contract


class EveCharacterManager(models.Manager):
    def get_or_create_by_id(self, character_id):
        try:
            return self.model.objects.get(id=character_id)
        except self.model.DoesNotExist:
            character_data = ESI.get_client().request(
                ESI['get_characters_character_id'](character_id=character_id)
            ).data

            character = EveCharacter(
                id=character_id,
                name=character_data['name']
            )

            character.save()

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

    icon_id = models.IntegerField()
    unit_str = models.CharField(max_length=16)

    @property
    def icon_path(self):
        return "/img/attributes/%d.png" % self.id

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

    def __str__(self):
        return self.name


class ModuleManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .prefetch_related(
                'moduleattribute_set__attribute',
                'type',
                'creator'
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

    mutator_type_id = models.IntegerField()
    source_type_id = models.IntegerField()

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

    @property
    def attribute_list(self):
        return sorted(
            [
                x for x in self.moduleattribute_set
                .annotate(
                    relevant=Subquery(
                        TypeAttribute.objects
                        .filter(
                            type=self.type,
                            attribute=OuterRef('attribute')
                        )
                        .values('display')[:1]
                    )
                )
                .filter(relevant=True)
            ],
            key=lambda x: x.attribute_id
        )


class ModuleAttribute(models.Model):
    module = models.ForeignKey(Module, models.CASCADE)
    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)

    value = models.FloatField()

    @property
    def real_value(self):
        if self.attribute.id == 73:
            return self.value / 1000
        elif self.attribute.id == 1795:
            return self.value / 1000
        elif self.attribute.id == 147:
            return self.value * 100
        else:
            return self.value


class TypeAttribute(models.Model):
    type = models.ForeignKey(ModuleType, models.CASCADE)
    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)

    display = models.BooleanField(default=False)
    high_is_good = models.NullBooleanField()
