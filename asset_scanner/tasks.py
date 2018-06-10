from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task

from eve_auth.models import EveUser
from abyssal_modules.models import ModuleType, Module
from abyssal_modules.tasks import create_module


@db_task(retries=1000, retry_delay=60)
def scan_assets_for_user(character_id):
    user = EveUser.objects.get(character_id=character_id)

    try:
        assets = user.get_assets()
    except EveUser.KeyDeletedException:
        return

    abyssal_types = ModuleType.objects.values_list('id', flat=True)
    abyssal_modules = [x for x in assets if x['type_id'] in abyssal_types]

    for x in abyssal_modules:
        if not Module.objects.filter(id=x['item_id']).exists():
            create_module(x['type_id'], x['item_id'])


@db_periodic_task(crontab(hour='*/2'))
def scan_assets_for_all_users():
    for u in EveUser.objects.filter(scope_read_assets=True):
        scan_assets_for_user(u.character_id)
