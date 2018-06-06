from django.db import models

from eve_esi import ESI


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

class Module(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.ForeignKey(
        ModuleType,
        models.CASCADE,
        related_name='modules',
        db_index=True
    )

    mutator_type_id = models.IntegerField()
    source_type_id = models.IntegerField()

    creator_id = models.BigIntegerField()

    attributes = models.ManyToManyField(
        ModuleDogmaAttribute,
        through='ModuleAttribute',
        related_name='+'
    )

    @property
    def attribute_list(self):
        return self.moduleattribute_set.filter(attribute__interesting=True).order_by('attribute_id')

class ModuleAttribute(models.Model):
    module = models.ForeignKey(Module, models.CASCADE)
    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)

    value = models.FloatField()

    @property
    def real_value(self):
        if self.attribute.id == 73:
            return self.value / 1000

        return self.value
