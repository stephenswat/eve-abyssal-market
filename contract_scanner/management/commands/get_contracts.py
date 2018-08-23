from django.core.management.base import BaseCommand

from contract_scanner.tasks import scan_public_contracts


class Command(BaseCommand):
    help = 'Updates all public contracts'

    def handle(self, *args, **options):
        scan_public_contracts()
