from django.db import models


class Mutator(models.Model):
    item_type = models.OneToOneField(
        "eve_sde.InvType", models.CASCADE, related_name="+"
    )
    result = models.ForeignKey("ModuleType", models.CASCADE)

    applicable_modules = models.ManyToManyField("eve_sde.InvType")
    attributes = models.ManyToManyField("TypeAttribute", through="MutatorAttribute")


class MutatorAttribute(models.Model):
    mutator = models.ForeignKey("Mutator", models.CASCADE)
    attribute = models.ForeignKey("TypeAttribute", models.CASCADE)

    min_modifier = models.DecimalField(max_digits=10, decimal_places=5)
    max_modifier = models.DecimalField(max_digits=10, decimal_places=5)
