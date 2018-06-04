from django.db import models


class ModuleDogmaAttribute(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    high_is_good = models.NullBooleanField()
    icon_id = models.IntegerField()
    unit_str = models.CharField(max_length=16)

    interesting = models.BooleanField()

    def __str__(self):
        return self.name

class ModuleType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)

    attributes = models.ManyToManyField(ModuleDogmaAttribute, related_name='+')

    def __str__(self):
        return self.name
