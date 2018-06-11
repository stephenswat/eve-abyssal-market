from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task

import logging

from django.db import transaction

from eve_auth.models import EveUser
from abyssal_modules.models import ModuleType, Module, EveCharacter, OwnershipRecord
from abyssal_modules.tasks import create_module


logger = logging.getLogger(__name__)


@db_task(retries=1000, retry_delay=60)
def scan_assets_for_user(character_id):
    user = EveUser.objects.get(character_id=character_id)
    character = EveCharacter.objects.get_or_create_by_id(character_id)

    try:
        assets = user.get_assets()
    except EveUser.KeyDeletedException:
        logger.info("Key refresh error for user %d", character_id)
        return

    abyssal_types = ModuleType.objects.values_list('id', flat=True)
    abyssal_modules = [x for x in assets if x['type_id'] in abyssal_types]

    found = []

    for x in abyssal_modules:
        try:
            module = Module.objects.get(id=x['item_id'])
        except Module.DoesNotExist:
            module = create_module(x['type_id'], x['item_id'])(blocking=True)

        found.append(module)

    with transaction.atomic():
        for m in found:
            m.set_ownership(character=character)

        for lost in (
            OwnershipRecord.uncompleted
            .filter(asset_owner=character_id)
            .exclude(module__id__in=[x.id for x in found])
        ):
            lost.complete()



@db_periodic_task(crontab(minute='0', hour='*/2'))
def scan_assets_for_all_users():
    for u in EveUser.objects.filter(scope_read_assets=True):
        scan_assets_for_user(u.character_id)
