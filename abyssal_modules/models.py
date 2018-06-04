from django.db import models

from eve_esi import ESI


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

    @classmethod
    def get_or_create_from_type_item_id(cls, type_id, item_id):
        try:
            return cls.objects.get(id=item_id)
        except cls.DoesNotExist:
            pass

        client = ESI.get_client()

        module_data = client.request(
            ESI['get_dogma_dynamic_items_type_id_item_id'](
                type_id=type_id,
                item_id=item_id
            )
        ).data

        res = cls(
            id=item_id,
            type_id=type_id,
            mutator_type_id=module_data['mutator_type_id'],
            source_type_id=module_data['source_type_id'],
            creator_id=module_data['created_by']
        )

        res.save()

        for a in module_data['dogma_attributes']:
            try:
                ModuleAttribute(
                    module=res,
                    attribute=ModuleDogmaAttribute.objects.get(id=a['attribute_id']),
                    value=a['value']
                ).save()
            except ModuleDogmaAttribute.DoesNotExist:
                pass

class ModuleAttribute(models.Model):
    module = models.ForeignKey(Module, models.CASCADE)
    attribute = models.ForeignKey(ModuleDogmaAttribute, models.CASCADE)

    value = models.FloatField()
