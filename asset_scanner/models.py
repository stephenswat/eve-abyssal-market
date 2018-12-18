from django.db import models

from eve_auth.models import EveUser
from abyssal_modules.models.modules import Module


class AssetRecord(models.Model):
    owner = models.ForeignKey(EveUser, models.CASCADE, related_name='asset_records')
    module = models.ForeignKey(Module, models.CASCADE, related_name='ownership_records')
