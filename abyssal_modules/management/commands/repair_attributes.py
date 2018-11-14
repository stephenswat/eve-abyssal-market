from django.core.management.base import BaseCommand

from abyssal_modules.models import ModuleDogmaAttribute


class Command(BaseCommand):
    help = 'Imports abyssal types and attributes'

    def handle(self, *args, **options):
        ModuleDogmaAttribute.objects.filter(id=204).update(
            name="Rate of Fire Bonus"
        )

        ModuleDogmaAttribute.objects.filter(id=2267).update(
            name="Capacitor Warfare Resistance"
        )

        ModuleDogmaAttribute.objects.filter(id=64).update(
            unit_str="%"
        )
