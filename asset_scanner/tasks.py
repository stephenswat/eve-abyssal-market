import logging

from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task

from django.db import transaction

from abyssal_modules.models import ModuleType
from eve_esi import ESI
from abyssal_modules.tasks import create_module
from eve_auth.models import EveUser
from asset_scanner.models import AssetRecord


logger = logging.getLogger(__name__)


@db_task(retries=10, retry_delay=300)
def read_assets_for_character(character):
    valid_module_types = {
        x for x in ModuleType.objects.values_list('id', flat=True)
    }

    items = ESI.request(
        'get_characters_character_id_assets',
        client=character.get_client(),
        multi_page=True,
        character_id=character.character_id
    )

    abyssal_modules = [
        x for x in items
        if x['type_id'] in valid_module_types
    ]

    with transaction.atomic():
        AssetRecord.objects.filter(owner=character).delete()

        for x in abyssal_modules:
            AssetRecord(
                owner=character,
                module=create_module.call_local(x['type_id'], x['item_id'])
            ).save()


@db_periodic_task(crontab(minute='30', hour='*/2'))
def read_all_assets():
    for x in EveUser.objects.filter(scope_read_assets=True):
        read_assets_for_character(x)
