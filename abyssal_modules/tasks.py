import logging

from django.db import transaction, connection

from huey import crontab
from huey.contrib.djhuey import db_task, db_periodic_task

from abyssal_modules.metrics import COUNTER_MODULES_CREATED
from abyssal_modules.models.modules import Module
from abyssal_modules.models.attributes import (
    ModuleAttribute,
    ModuleDogmaAttribute,
    TypeAttribute,
)
from abyssal_modules.models.characters import EveCharacter
from eve_esi import ESI, EsiException


logger = logging.getLogger(__name__)


@db_task(retries=1000, retry_delay=60)
def create_module(type_id, item_id, force=False):
    if not force:
        try:
            return Module.objects.get(id=item_id)
        except Module.DoesNotExist:
            pass

    try:
        module_data = ESI.request(
            "get_dogma_dynamic_items_type_id_item_id", type_id=type_id, item_id=item_id
        ).data
    except EsiException as e:
        logger.exception(
            "Retrieval of stats for module %d failed (status %d)", item_id, e.status
        )
        return

    with transaction.atomic():
        character = EveCharacter.objects.get_or_create_by_id(module_data["created_by"])

        res, created = Module.objects.get_or_create(
            id=item_id,
            defaults={
                "type_id": type_id,
                "mutator_id": module_data["mutator_type_id"],
                "source_id": module_data["source_type_id"],
                "creator": character,
            },
        )

        if created:
            COUNTER_MODULES_CREATED.labels(type=type_id).inc()

        for a in module_data["dogma_attributes"]:
            try:
                ModuleAttribute(
                    module=res,
                    attribute=ModuleDogmaAttribute.objects.get(id=a["attribute_id"]),
                    new_attribute=TypeAttribute.objects.get(
                        type_id=type_id, attribute_id=a["attribute_id"]
                    ),
                    value=a["value"],
                ).save()
            except (ModuleDogmaAttribute.DoesNotExist, TypeAttribute.DoesNotExist):
                pass

    return res


@db_periodic_task(crontab(minute="0", hour="0"))
def materialize_ratings():
    with connection.cursor() as cursor:
        cursor.execute(
            "REFRESH MATERIALIZED VIEW abyssal_modules_attribute_stats__view;"
        )
