from django.core.management.base import BaseCommand

from asset_scanner.tasks import scan_assets_for_all_users


class Command(BaseCommand):
    help = 'Imports abyssal types and attributes'

    def handle(self, *args, **options):
        scan_assets_for_all_users()
