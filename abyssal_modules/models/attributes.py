from django.db import models
from django.db.models import F, Value, Case, When, FloatField


DERIVED_ATTRIBUTES = {
    100000: {
        'types': [47781, 47785, 47789, 47793, 47836, 47838, 47840],
        'name': 'Shield boost per second',
        'unit_str': 'HP/s',
        'value': lambda x: x.get_value(68) / x.get_value(10073),
        'high_is_good': True
    },
    100001: {
        'types': [47769, 47773, 47777, 47842, 47844, 47846],
        'name': 'Armor repair per second',
        'unit_str': 'HP/s',
        'value': lambda x: x.get_value(84) / x.get_value(10073),
        'high_is_good': True
    },
    100002: {
        'types': [47781, 47785, 47789, 47793],
        'name': 'Shield boost per capacitor',
        'unit_str': 'HP/GJ',
        'value': lambda x: x.get_value(68) / x.get_value(6),
        'high_is_good': True
    },
    100003: {
        'types': [47769, 47773, 47777, 47842, 47844, 47846],
        'name': 'Armor repair per capacitor',
        'unit_str': 'HP/GJ',
        'value': lambda x: x.get_value(84) / x.get_value(6),
        'high_is_good': True
    },
    100004: {
        'types': [49730, 49722, 49726, 49734],
        'name': 'DPS Bonus',
        'unit_str': '%',
        'value': lambda x: ((x.get_value(64) * 1 / (1 - x.get_value(10204) / 100)) - 1) * 100,
        'high_is_good': True
    },
    100005: {
        'types': [49738],
        'name': 'DPS Bonus',
        'unit_str': '%',
        'value': lambda x: (((x.get_value(10213) / 100 + 1) / (1 - (x.get_value(10204) / 100))) - 1) * 100,
        'high_is_good': True
    },
}


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
        return getattr(self, '_derived', False)

    def __str__(self):
        return self.name


class UnratedModuleAttributeManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .prefetch_related(
                'new_attribute',
                'new_attribute__type',
                'new_attribute__attribute',
                'attribute',
                'module',
                'static_module'
            )
        )


class ModuleAttributeManager(UnratedModuleAttributeManager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .annotate(
                rating=(
                    Case(
                        When(new_attribute__aggregates__stddev=0, then=Value(0, output_field=FloatField())),
                        default=(
                            F('value') - F('new_attribute__aggregates__avg')
                        ) / F('new_attribute__aggregates__stddev')
                    ) * Value(4) * Case(
                        When(new_attribute__high_is_good=True, then=Value(1)),
                        default=Value(-1)
                    )
                )
            )
        )


class ModuleAttributeAggregate(models.Model):
    new_attribute = models.OneToOneField(
        'TypeAttribute', models.DO_NOTHING, primary_key=True, related_name='aggregates'
    )

    avg = models.FloatField()
    stddev = models.FloatField()

    class Meta:
        managed = False
        db_table = 'abyssal_modules_attribute_stats__view'


class ModuleAttributeView(models.Model):
    module = models.ForeignKey('Module', models.CASCADE, null=True, related_name='attribute_values')
    static_module = models.ForeignKey('StaticModule', models.CASCADE, null=True, related_name='attribute_values')

    attribute = models.ForeignKey('ModuleDogmaAttribute', models.CASCADE)
    new_attribute = models.ForeignKey('TypeAttribute', models.CASCADE)

    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'abyssal_modules_derived_attributes__view'

    objects = ModuleAttributeManager()
    unrated = UnratedModuleAttributeManager()

    def rounded_rating(self):
        return int(round(self.rating))


class ModuleAttribute(models.Model):
    module = models.ForeignKey('Module', models.CASCADE, null=True)
    static_module = models.ForeignKey('StaticModule', models.CASCADE, null=True)

    attribute = models.ForeignKey('ModuleDogmaAttribute', models.CASCADE)
    new_attribute = models.ForeignKey('TypeAttribute', models.CASCADE)

    value = models.FloatField(db_index=True)


class TypeAttribute(models.Model):
    type = models.ForeignKey('ModuleType', models.CASCADE)
    attribute = models.ForeignKey('ModuleDogmaAttribute', models.CASCADE)

    display = models.BooleanField(default=False)
    high_is_good = models.NullBooleanField()

    @property
    def pyfa_display(self):
        return self.attribute_id in {
            1795, 6, 1159, 20, 796, 30, 554, 50, 54, 64, 67, 68, 72, 73, 204,
            84, 213, 983, 90, 2267, 97
        }
