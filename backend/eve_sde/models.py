from django.db import models


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Constellation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    region = models.ForeignKey(Region, models.DO_NOTHING, db_index=True)

    def __str__(self):
        return self.name


class SolarSystem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    constellation = models.ForeignKey(Constellation, models.DO_NOTHING, db_index=True)

    gates = models.ManyToManyField("self")

    def __str__(self):
        return self.name


class InvType(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=128)
