import logging
import pprint

from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task

from django.db import transaction
from django.db.models import Q

from abyssal_modules.models import ModuleType
from eve_auth.models import EveUser
from contract_scanner.models import Contract
from eve_esi import ESI
from abyssal_modules.tasks import create_module_helper


logger = logging.getLogger(__name__)


@db_task(retries=10, retry_delay=60)
def scan_contract(contract_dict, region_id):
    abyssal_ids = list(ModuleType.objects.values_list('id', flat=True))

    client = ESI.get_client()

    with transaction.atomic():
        contract, _ = Contract.objects.get_or_create(
            id=contract_dict['contract_id'],
            defaults={
                'issuer_id': contract_dict['issuer_id'],
                'price': contract_dict['price'],
                'issued_at': contract_dict['date_issued'].v,
                'expires_at': contract_dict['date_expired'].v,
                'single_item': False,
                'location_id': contract_dict['start_location_id'],
                'region_id': region_id,
                'auction': (contract_dict['type'] == 'auction')
            }
        )

        contract.available = True

        req = client.request(
            ESI['get_contracts_public_items_contract_id'](contract_id=contract.id)
        )

        # This happens if a contract is deleted.
        if req.status == 404:
            return

        # Not totally sure when this happens...
        if req.status == 403:
            return

        # This prevents us from shitting the bed on contracts that are cached but have been accepted since
        if req.status == 204 and req.data is None:
            return

        data = req.data

        contract.single_item = (len(data) == 1)

        for item in data:
            if item['type_id'] in abyssal_ids:
                logger.info(
                    "Found abyssal module %d in contract %d.",
                    item['item_id'], contract_dict['contract_id']
                )

                module = create_module_helper(
                    type_id=item['type_id'],
                    item_id=item['item_id']
                )

                contract.modules.add(module)

        contract.save()


@db_periodic_task(crontab(minute='0,30'))
def scan_public_contracts(scan_all=False):
    client = ESI.get_client()

    all_regions = client.request(ESI['get_universe_regions']()).data
    all_contract_ids = set()

    for region in all_regions:
        head = client.head(
            ESI['get_contracts_public_region_id'](region_id=region)
        )

        number_of_page = head.header['X-Pages'][0]

        for page in range(1, number_of_page + 1):
            contracts = list(client.request(
                ESI['get_contracts_public_region_id'](region_id=region, page=page)
            ).data)

            for contract_dict in contracts:
                all_contract_ids.add(contract_dict['contract_id'])

                if contract_dict['type'] not in ['item_exchange', 'auction']:
                    continue

                try:
                    contract = Contract.objects.get(id=contract_dict['contract_id'])

                    if not contract.available:
                        contract.available = True
                        contract.save()

                    if scan_all:
                        scan_contract(dict(contract_dict), region)
                except Contract.DoesNotExist:
                    scan_contract(dict(contract_dict), region)

    Contract.objects.filter(
        Q(available=True) & ~Q(id__in=all_contract_ids)
    ).update(
        available=False
    )

