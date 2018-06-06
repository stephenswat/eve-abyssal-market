from django.db import transaction

from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task

from abyssal_modules.models import Module, ModuleAttribute, ModuleDogmaAttribute
from eve_esi import ESI


@db_task(retries=1000, retry_delay=60)
def create_module(type_id, item_id):
    if Module.objects.filter(id=item_id).exists():
        return

    client = ESI.get_client()

    module_data = client.request(
        ESI['get_dogma_dynamic_items_type_id_item_id'](
            type_id=type_id,
            item_id=item_id
        )
    ).data

    with transaction.atomic():
        res = Module(
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
