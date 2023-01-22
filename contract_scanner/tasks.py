import logging
import requests
import datetime

from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task

from django.db import transaction
from django.db.models import Q

from abyssal_modules.models.modules import ModuleType
from contract_scanner.models import Contract, PlexPriceRecord
from contract_scanner.metrics import COUNTER_CONTRACTS_FOUND, COUNTER_CONTRACTS_SCANNED
from eve_esi import ESI
from abyssal_modules.tasks import create_module


logger = logging.getLogger(__name__)


@db_task(retries=10, retry_delay=60)
def scan_contract(contract_dict, region_id):
    abyssal_ids = list(ModuleType.objects.values_list("id", flat=True))

    COUNTER_CONTRACTS_SCANNED.labels(region=region_id, type=contract_dict["type"]).inc()

    with transaction.atomic():
        contract, _ = Contract.objects.get_or_create(
            id=contract_dict["contract_id"],
            defaults={
                "issuer_id": contract_dict["issuer_id"],
                "price": contract_dict["price"],
                "issued_at": contract_dict["date_issued"].v,
                "expires_at": contract_dict["date_expired"].v,
                "single_item": False,
                "location_id": contract_dict["start_location_id"],
                "region_id": region_id,
                "auction": (contract_dict["type"] == "auction"),
            },
        )

        contract.available = True

        req = ESI.request(
            "get_contracts_public_items_contract_id", contract_id=contract.id
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
        items = 0

        contract.single_item = True
        contract.plex = 0

        for item in data:
            if item["type_id"] in abyssal_ids and item.get("is_included", True):
                items += 1

                logger.info(
                    "Found abyssal module %d in contract %d.",
                    item["item_id"],
                    contract_dict["contract_id"],
                )

                module = create_module.call_local(
                    type_id=item["type_id"], item_id=item["item_id"]
                )

                contract.modules.add(module)
            elif item["type_id"] == 44992 and not item["is_included"]:
                contract.plex += item["quantity"]
            else:
                items += 1

        contract.single_item = items == 1

        contract.save()


@db_periodic_task(crontab(minute="0,30"), priority=800)
def scan_public_contracts(scan_all=False):
    if (
        datetime.time(hour=10, minute=55)
        <= datetime.datetime.now(datetime.timezone.utc).time()
        <= datetime.time(hour=11, minute=20)
    ):
        return

    all_regions = ESI.request("get_universe_regions").data
    all_contract_ids = set()

    for region in all_regions:
        number_of_page = ESI.head(
            "get_contracts_public_region_id", region_id=region
        ).header["X-Pages"][0]

        for page in range(1, number_of_page + 1):
            req = ESI.request(
                "get_contracts_public_region_id", region_id=region, page=page
            )

            contracts = list(req.data)

            for contract_dict in contracts:
                all_contract_ids.add(contract_dict["contract_id"])

                if contract_dict["type"] not in ["item_exchange", "auction"]:
                    continue

                COUNTER_CONTRACTS_FOUND.labels(
                    region=region, type=contract_dict["type"]
                ).inc()

                try:
                    contract = Contract.objects.get(id=contract_dict["contract_id"])

                    if not contract.available:
                        contract.available = True
                        contract.save()

                    if scan_all:
                        scan_contract(dict(contract_dict), region)
                except Contract.DoesNotExist:
                    scan_contract(dict(contract_dict), region)

    Contract.objects.filter(Q(available=True) & ~Q(id__in=all_contract_ids)).update(
        available=False
    )


@db_periodic_task(crontab(minute="0", hour="*"))
def update_plex_price():
    req = requests.get(
        "https://api.evemarketer.com/ec/marketstat/json?typeid=44992&regionlimit=10000002"
    ).json()

    price = int(req[0]["buy"]["fivePercent"])

    PlexPriceRecord(price=price).save()
