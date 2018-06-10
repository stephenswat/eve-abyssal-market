import pprint
import logging

from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task

from eve_auth.models import EveUser
from contract_scanner.models import Contract


logger = logging.getLogger(__name__)


CONTRACT_STATUS = {
    'outstanding': 0,
    'in_progress': 0,
    'finished_issuer': 2,
    'finished_contractor': 2,
    'finished': 2,
    'cancelled': 4,
    'rejected': 5,
    'failed': 9,
    'deleted': 6,
    'reversed': 9
}


@db_task(retries=1000, retry_delay=60)
def scan_contract(character_id, contract_id):
    user = EveUser.objects.get(character_id=character_id)
    logger.info("Not scanning contract %d for user %d (not implemented)", contract_id, character_id)


@db_task(retries=1000, retry_delay=60)
def scan_contracts_for_user(character_id):
    user = EveUser.objects.get(character_id=character_id)

    try:
        contracts = user.get_contracts()
    except EveUser.KeyDeletedException:
        logger.info("Key refresh error for user %d", character_id)
        return

    all_ids = set()

    for x in contracts:
        if x['type'] != 'item_exchange':
            continue

        if x['issuer_id'] != character_id:
            continue

        if x['availability'] != 'public':
            continue

        all_ids.add(x['contract_id'])

        obj, _ = Contract.objects.update_or_create(
            id=x['contract_id'],
            defaults={
                'owner': user,
                'issuer_id': x['issuer_id'],
                'price': x['price'],
                'issued_at': x['date_issued'].v,
                'expires_at': x['date_expired'].v,
                'status': CONTRACT_STATUS[x['status']]
            }
        )

        if not obj.known:
            scan_contract(character_id, obj.id)


@db_periodic_task(crontab(hour='*/2'))
def scan_contracts_for_all_users():
    for u in EveUser.objects.filter(scope_read_contracts=True):
        scan_contracts_for_user(u.character_id)
