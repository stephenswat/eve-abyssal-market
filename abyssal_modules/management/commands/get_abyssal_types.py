from tqdm import tqdm

from django.core.management.base import BaseCommand

from eve_esi import ESI
from abyssal_modules.models import ModuleType, ModuleDogmaAttribute
from ._abyssal_primitive import ITEMS, UNIT_STR


class Command(BaseCommand):
    help = 'Imports abyssal types and attributes'

    INTERESTING = [
        6, 20, 30, 50, 54, 67, 68, 72, 73, 84, 97, 105, 554, 983, 1159, 2044, 2267
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = ESI.get_client()

    def handle(self, *args, **options):
        for i in tqdm(ITEMS):
            type_obj, _ = ModuleType.objects.update_or_create(
                id=i['abyssal_id'],
                defaults={'name': i['name']}
            )

            items = self.client.request(
                ESI['get_universe_types_type_id'](type_id=i['normal_id'])
            ).data['dogma_attributes']

            for a in items:
                self.scan_item(a['attribute_id'], type_obj)

    def scan_item(self, item_id, item_type):
        attr_data = self.client.request(
            ESI['get_dogma_attributes_attribute_id'](attribute_id=item_id)
        ).data

        if not attr_data.get('published', False):
            return

        attr_obj, _ = ModuleDogmaAttribute.objects.update_or_create(
            id=attr_data['attribute_id'],
            defaults={
                'name': attr_data['display_name'],
                'high_is_good': attr_data.get('high_is_good', None),
                'icon_id': attr_data.get('icon_id', 0),
                'unit_str': UNIT_STR.get(attr_data.get('unit_id', -1), ''),
                'interesting': attr_data['attribute_id'] in self.INTERESTING
            }
        )

        item_type.attributes.add(attr_obj)
