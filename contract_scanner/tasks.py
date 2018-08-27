import logging
import pprint

from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task

from django.db import transaction

from abyssal_modules.models import ModuleType
from eve_auth.models import EveUser
from contract_scanner.models import Contract
from eve_esi import ESI
from abyssal_modules.tasks import create_module_helper


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
def scan_contract(contract_dict):
    abyssal_ids = list(ModuleType.objects.values_list('id', flat=True))

    client = ESI.get_client()

    with transaction.atomic():
        contract, _ = Contract.objects.get_or_create(
            id=contract_dict['contract_id'],
            defaults={
                'status': 0,
                'issuer_id': contract_dict['issuer_id'],
                'price': contract_dict['price'],
                'issued_at': contract_dict['date_issued'].v,
                'expires_at': contract_dict['date_expired'].v,
                'single_item': False
            }
        )
        contract.scanned = True
        contract.status = 0

        data = client.request(
            ESI['get_contracts_public_items_contract_id'](contract_id=contract.id)
        ).data

        contract.single_item = (len(data) == 1)

        for item in data:
            if item['type_id'] in abyssal_ids:
                print("Abyssal!")
                module = create_module_helper(
                    type_id=item['type_id'],
                    item_id=item['item_id']
                )

                contract.modules.add(module)

        contract.save()


@db_periodic_task(crontab(minute='0', hour='*/1'))
def scan_public_contracts():
    client = ESI.get_client()

    head = client.head(
        ESI['get_contracts_public_region_id'](region_id=10000002)
    )

    all_contracts = []

    if head.status == 200:
        number_of_page = head.header['X-Pages'][0]

        for page in range(1, number_of_page + 1):
            data = client.request(
                ESI['get_contracts_public_region_id'](region_id=10000002, page=page)
            )

            all_contracts += list(data.data)

    for contract_dict in all_contracts:
        if contract_dict['type'] != 'item_exchange':
            continue

        try:
            contract = Contract.objects.get(id=contract_dict['contract_id'])

            if not contract.scanned:
                raise ValueError("Contract is not yet scanned")
        except (Contract.DoesNotExist, ValueError) as e:
            scan_contract(dict(contract_dict))

