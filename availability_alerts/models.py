from django.db import models

from eve_auth.models import EveUser
from abyssal_modules.models import ModuleType, ModuleDogmaAttribute


class AlertRequest(models.Model):
    owner = models.ForeignKey(EveUser, models.CASCADE)
    type = models.ForeignKey(ModuleType, models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    attributes = models.ManyToManyField(ModuleDogmaAttribute, through='AlertRequestAttributes')


class AlertRequestAttributes(models.Model):
    request = models.ForeignKey(AlertRequest, models.CASCADE)
    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)

    min_value = models.FloatField(null=True)
    max_value = models.FloatField(null=True)
