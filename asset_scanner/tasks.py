from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task

from eve_auth.models import EveUser
from abyssal_modules.models import ModuleType, Module


@db_task(retries=1000, retry_delay=60)
def scan_assets_for_user(character_id):
    user = EveUser.objects.get(character_id=character_id)
    assets = user.get_assets()

    abyssal_types = ModuleType.objects.values_list('id', flat=True)
    abyssal_modules = [x for x in assets if x['type_id'] in abyssal_types]

    for x in abyssal_modules:
        Module.get_or_create_from_type_item_id(x['type_id'], x['item_id'])


@db_periodic_task(crontab(minute='*'))
def scan_assets_for_all_users():
    for u in EveUser.objects.filter(scope_read_assets=True):
        scan_assets_for_user(u.character_id)
