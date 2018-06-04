from tqdm import tqdm

from django.core.management.base import BaseCommand

from ._abyssal_primitive import ITEMS, UNIT_STR
from eve_esi import ESI
from abyssal_modules.models import ModuleType, ModuleDogmaAttribute


class Command(BaseCommand):
    help = 'Imports abyssal types and attributes'

    def handle(self, *args, **options):
        client = ESI.get_client()

        INTERESTING = [6, 20, 30, 50, 54, 68, 72, 73, 84, 97, 105, 554, 983, 1159, 2044]

        for i in tqdm(ITEMS):
            type_obj, _ = ModuleType.objects.update_or_create(
                id=i['abyssal_id'],
                defaults={
                    'name': i['name']
                }
            )

            for a in client.request(
                ESI['get_universe_types_type_id'](type_id=i['normal_id'])
            ).data['dogma_attributes']:
                attr_data = client.request(
                    ESI['get_dogma_attributes_attribute_id'](attribute_id=a['attribute_id'])
                ).data

                if not attr_data.get('published', False):
                    continue

                attr_obj, _ = ModuleDogmaAttribute.objects.update_or_create(
                    id=attr_data['attribute_id'],
                    defaults={
                        'name': attr_data['display_name'],
                        'high_is_good': attr_data.get('high_is_good', None),
                        'icon_id': attr_data.get('icon_id', 0),
                        'unit_str': UNIT_STR.get(attr_data.get('unit_id', -1), ''),
                        'interesting': attr_data['attribute_id'] in INTERESTING
                    }
                )

                type_obj.attributes.add(attr_obj)

