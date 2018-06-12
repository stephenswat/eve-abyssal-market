from django.db import models
from django.utils import timezone
from django.db import transaction

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

    high_is_good = models.NullBooleanField()
    icon_id = models.IntegerField()
    unit_str = models.CharField(max_length=16)

    interesting = models.BooleanField()

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
        related_name='+'
    )

    def __str__(self):
        return self.name

class ModuleManager(models.Manager):
    def get_queryset(self):
        return super(ModuleManager, self).get_queryset().prefetch_related(
            'moduleattribute_set__attribute',
            'ownershiprecord_set__asset_owner',
            'ownershiprecord_set__contract_contract',
            'type',
            'creator'
        )


class Module(models.Model):
    objects = ModuleManager()

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
            [x for x in self.moduleattribute_set.all() if x.attribute.interesting],
            key=lambda x: x.attribute_id
        )

    @property
    def current_ownership(self):
        for ownership in self.ownershiprecord_set.all():
            if ownership.end == None:
                return ownership
        return None

    @transaction.atomic
    def set_ownership(self, character=None, contract=None):
        if sum(x is not None for x in [character, contract]) != 1:
            raise ValueError("Must pass either a character or a contract")

        if character is not None:
            params = {'asset_owner': character}
        elif contract is not None:
            params = {'contract_contract': contract}

        try:
            existing = OwnershipRecord.uncompleted.get(module=self)

            if character is not None and existing.asset_owner == character:
                print("1")
                return
            elif contract is not None and existing.contract_contract == contract:
                print("2")
                return
            else:
                print("3")
                existing.complete()
                OwnershipRecord(module=self, **params).save()
        except OwnershipRecord.DoesNotExist:
            print("4")
            OwnershipRecord(module=self, **params).save()


class ModuleAttribute(models.Model):
    module = models.ForeignKey(Module, models.CASCADE)
    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)

    value = models.FloatField()

    @property
    def real_value(self):
        if self.attribute.id == 73:
            return self.value / 1000

        return self.value


class UncompetedOwnershipRecordManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(end=None)

class OwnershipRecord(models.Model):
    objects = models.Manager()
    uncompleted = UncompetedOwnershipRecordManager()

    module = models.ForeignKey(
        Module,
        models.CASCADE,
        db_index=True
    )

    asset_owner = models.ForeignKey(
        EveCharacter,
        models.CASCADE,
        null=True,
        db_index=True
    )
    contract_contract = models.ForeignKey(
        Contract,
        models.CASCADE,
        null=True,
        db_index=True
    )

    start = models.DateTimeField(auto_now_add=True, db_index=True)
    end = models.DateTimeField(null=True, db_index=True)

    def complete(self):
        self.end = timezone.now()
        self.save()
