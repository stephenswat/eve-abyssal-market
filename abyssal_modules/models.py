from django.db import models

from eve_esi import ESI


class EveCharacterManager(models.Manager):
    def upsert_by_id(self, character_id):
        client = ESI.get_client()

        character_data = client.request(
            ESI['get_characters_character_id'](character_id=character_id)
        ).data

        character, _ = EveCharacter.objects.update_or_create(
            id=character_id,
            defaults={'name': character_data['name']}
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

class ModuleAttribute(models.Model):
    module = models.ForeignKey(Module, models.CASCADE)
    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)

    value = models.FloatField()

    @property
    def real_value(self):
        if self.attribute.id == 73:
            return self.value / 1000

        return self.value
