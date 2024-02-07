from django.db import models
from django.db.models import F, Value, Case, When, FloatField


class ModuleDogmaAttribute(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=64)

    unit_str = models.CharField(max_length=16)

    is_derived = models.BooleanField(default=False)

    @property
    def icon_path(self):
        return "/img/attributes/%d.png" % self.id

    @property
    def derived(self):
        return getattr(self, "_derived", False)

    def __str__(self):
        return self.name


class UnratedModuleAttributeManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .prefetch_related(
                "new_attribute",
                "new_attribute__type",
                "new_attribute__attribute",
                "attribute",
                "module",
                "static_module",
            )
        )


class ModuleAttributeManager(UnratedModuleAttributeManager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                rating=(
                    Case(
                        When(
                            new_attribute__aggregates__stddev=0,
                            then=Value(0, output_field=FloatField()),
                        ),
                        default=(F("value") - F("new_attribute__aggregates__avg"))
                        / F("new_attribute__aggregates__stddev"),
                    )
                    * Value(4)
                    * Case(
                        When(new_attribute__high_is_good=True, then=Value(1)),
                        default=Value(-1),
                    )
                )
            )
        )


class ModuleAttributeAggregate(models.Model):
    new_attribute = models.OneToOneField(
        "TypeAttribute", models.DO_NOTHING, primary_key=True, related_name="aggregates"
    )

    avg = models.FloatField()
    stddev = models.FloatField()

    class Meta:
        managed = False
        db_table = "abyssal_modules_attribute_stats__view"


class ModuleAttributeView(models.Model):
    module = models.ForeignKey(
        "Module", models.CASCADE, null=True, related_name="attribute_values"
    )
    static_module = models.ForeignKey(
        "StaticModule", models.CASCADE, null=True, related_name="attribute_values"
    )

    attribute = models.ForeignKey("ModuleDogmaAttribute", models.CASCADE)
    new_attribute = models.ForeignKey("TypeAttribute", models.CASCADE)

    value = models.FloatField()

    class Meta:
        managed = False
        db_table = "abyssal_modules_derived_attributes__view"

    objects = ModuleAttributeManager()
    unrated = UnratedModuleAttributeManager()

    def rounded_rating(self):
        return int(round(self.rating))


class ModuleAttribute(models.Model):
    module = models.ForeignKey("Module", models.CASCADE, null=True)
    static_module = models.ForeignKey("StaticModule", models.CASCADE, null=True)

    attribute = models.ForeignKey("ModuleDogmaAttribute", models.CASCADE)
    new_attribute = models.ForeignKey("TypeAttribute", models.CASCADE)

    value = models.FloatField(db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=["module", "attribute"]),
            models.Index(fields=["module", "attribute", "-value"]),
            models.Index(fields=["module", "attribute", "value"]),
            models.Index(fields=["value"]),
            models.Index(fields=["-value"]),
            models.Index(
                F("attribute"), F("value").asc(), name="attribute_value_asc_idx"
            ),
            models.Index(
                F("attribute"), F("value").desc(), name="attribute_value_desc_idx"
            ),
        ]


class TypeAttribute(models.Model):
    type = models.ForeignKey("ModuleType", models.CASCADE)
    attribute = models.ForeignKey("ModuleDogmaAttribute", models.CASCADE)

    display = models.BooleanField(default=False)
    high_is_good = models.BooleanField(null=True)

    @property
    def pyfa_display(self):
        return self.attribute_id in {
            1795,
            6,
            1159,
            20,
            796,
            30,
            554,
            50,
            54,
            64,
            67,
            68,
            72,
            73,
            204,
            84,
            213,
            983,
            90,
            2267,
            97,
            974,
            975,
            976,
            977,
            1255,
            2307,
            2306,
            2347,
            2346,
            2336,
            2337,
            2338,
            2335,
            160,
            37,
            263,
            9,
            54,
            265,
            158,
        }
