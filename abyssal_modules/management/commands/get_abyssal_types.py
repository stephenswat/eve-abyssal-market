from tqdm import tqdm

from django.core.management.base import BaseCommand

from eve_esi import ESI
from abyssal_modules.models import ModuleType, ModuleDogmaAttribute, TypeAttribute
from ._abyssal_primitive import ITEMS, UNIT_STR


class Command(BaseCommand):
    help = 'Imports abyssal types and attributes'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = ESI.get_client()

    def handle(self, *args, **options):
        for i in tqdm(ITEMS):
            relevant = dict(i['relevant_attributes'])

            type_obj, _ = ModuleType.objects.update_or_create(
                id=i['abyssal_id'],
                defaults={'name': i['name']}
            )

            items = self.client.request(
                ESI['get_universe_types_type_id'](type_id=i['normal_id'])
            ).data['dogma_attributes']

            for a in items:
                attr_data = self.client.request(
                    ESI['get_dogma_attributes_attribute_id'](attribute_id=a['attribute_id'])
                ).data

                if not attr_data.get('published', False):
                    continue

                attr_obj, _ = ModuleDogmaAttribute.objects.update_or_create(
                    id=attr_data['attribute_id'],
                    defaults={
                        'name': attr_data['display_name'],
                        'icon_id': attr_data.get('icon_id', 0),
                        'unit_str': UNIT_STR.get(attr_data.get('unit_id', -1), ''),
                    }
                )

                TypeAttribute.objects.update_or_create(
                    type=type_obj,
                    attribute=attr_obj,
                    defaults={
                        'high_is_good': relevant.get(attr_data['attribute_id'], attr_data.get('high_is_good', None)),
                        'display': attr_data['attribute_id'] in relevant
                    }
                )
