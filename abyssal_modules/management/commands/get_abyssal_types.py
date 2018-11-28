from tqdm import tqdm
import requests

from django.core.management.base import BaseCommand

from eve_esi import ESI
from abyssal_modules.models import ModuleType, ModuleDogmaAttribute, TypeAttribute, Mutator, MutatorAttribute
from eve_sde.models import InvType
from ._abyssal_primitive import ITEMS, UNIT_STR


class Command(BaseCommand):
    help = 'Imports abyssal types and attributes'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = ESI.get_client()

    def import_types(self):
        for i in tqdm(ITEMS):
            relevant = dict(i['relevant_attributes'])

            type_obj, _ = ModuleType.objects.update_or_create(
                id=i['abyssal_id'],
                defaults={'name': i['name']}
            )

            items = ESI.request(
                'get_universe_types_type_id',
                client=self.client,
                type_id=i['normal_id']
            ).data['dogma_attributes']

            for a in items:
                attr_data = ESI.request(
                    'get_dogma_attributes_attribute_id',
                    client=self.client,
                    attribute_id=a['attribute_id']
                ).data

                if not attr_data.get('published', False):
                    continue

                attr_obj, _ = ModuleDogmaAttribute.objects.update_or_create(
                    id=attr_data['attribute_id'],
                    defaults={
                        'name': attr_data['display_name'],
                        'short_name': attr_data['name'],
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

    def repair_attributes(self):
        ModuleDogmaAttribute.objects.filter(id=204).update(
            name="Rate of Fire Bonus"
        )

        ModuleDogmaAttribute.objects.filter(id=2267).update(
            name="Capacitor Warfare Resistance"
        )

    def import_mutators(self):
        data = requests.get('http://sde.hoboleaks.space/tq/dynamicitemattributes.json').json()

        for mid, values in data.items():
            mutator, _ = Mutator.objects.update_or_create(
                item_type_id=int(mid),
                defaults={
                    'result_id': values['inputOutputMapping'][0]['resultingType']
                }
            )

            mutator.applicable_modules.set(
                InvType
                .objects
                .filter(
                    id__in=values['inputOutputMapping'][0]['applicableTypes']
                )
            )

            for attr_id, modifiers in values['attributeIDs'].items():
                attribute = TypeAttribute.objects.get(
                    type_id=values['inputOutputMapping'][0]['resultingType'],
                    attribute_id=attr_id
                )

                MutatorAttribute.objects.update_or_create(
                    mutator=mutator,
                    attribute=attribute,
                    defaults={
                        'min_modifier': round(modifiers['min'], 5),
                        'max_modifier': round(modifiers['max'], 5),
                    }
                )

    def handle(self, *args, **options):
        print("Importing types and attributes...")
        self.import_types()
        print("Repairing bad attributes...")
        self.repair_attributes()
        print("Importing mutators...")
        self.import_mutators()
