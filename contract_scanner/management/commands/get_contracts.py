from django.core.management.base import BaseCommand

from contract_scanner.tasks import scan_public_contracts


class Command(BaseCommand):
    help = 'Updates all public contracts'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--force', action='store_true', help='Force a rescan of all contracts')

    def handle(self, *args, **options):
        scan_public_contracts(scan_all=options['force'])
