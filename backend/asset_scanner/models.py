from django.db import models

from eve_auth.models import EveUser
from abyssal_modules.models.modules import Module


class Location(models.Model):
    TYPE_CHARACTER = 0
    # TYPE_CORPORATION = 1
    # TYPE_ALLIANCE = 2

    # TYPE_CHOICES = (
    #     (TYPE_CHARACTER, "Character"),
    #     (TYPE_CORPORATION, "Corporation"),
    #     (TYPE_ALLIANCE, "Alliance"),
    # )

    location_id = models.IntegerField(primary_key=True)
    station_id = models.ForeignKey("eve_sde.Station", models.SET_NULL, null=True)
    type_id = models.ForeignKey("eve_sde.InvType", models.CASCADE, related_name="+")
    owner = models.ForeignKey(EveUser, models.CASCADE, related_name="location_records", null=True)


class AssetRecord(models.Model):
    owner = models.ForeignKey(EveUser, models.CASCADE, related_name="asset_records")
    module = models.ForeignKey(Module, models.CASCADE, related_name="ownership_records")
    location = models.ForeignKey(Location, models.CASCADE, related_name="asset_records", null=True)
