from tqdm import tqdm
import requests
from collections import defaultdict

from django.core.management.base import BaseCommand

from eve_esi import ESI
from abyssal_modules.models.modules import ModuleType, StaticModule
from abyssal_modules.models.attributes import ModuleDogmaAttribute, TypeAttribute, ModuleAttribute, DERIVED_ATTRIBUTES
from abyssal_modules.models.mutators import Mutator, MutatorAttribute
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

    def create_derived(self):
        for attr_id, data in DERIVED_ATTRIBUTES.items():
            attr, _ = ModuleDogmaAttribute.objects.update_or_create(
                id=attr_id,
                defaults={
                    'name': data['name'],
                    'short_name': data['name'].lower().replace(' ', '_'),
                    'unit_str': data['unit_str'],
                    'is_derived': True
                }
            )

            for type_id in data['types']:
                TypeAttribute.objects.update_or_create(
                    type_id=type_id,
                    attribute=attr,
                    defaults={
                        'display': True,
                        'high_is_good': data['high_is_good']
                    }
                )

        for attr_id in [73, 1795, 147, 213, 204]:
            original = ModuleDogmaAttribute.objects.get(id=attr_id)

            new, _ = ModuleDogmaAttribute.objects.update_or_create(
                id=attr_id + 10000,
                defaults={
                    'name': original.name,
                    'short_name': 'display_' + original.short_name,
                    'unit_str': original.unit_str,
                    'is_derived': True
                }
            )

            for type_attr in original.typeattribute_set.all():
                TypeAttribute.objects.update_or_create(
                    attribute=new,
                    type=type_attr.type,
                    defaults={
                        'display': type_attr.display,
                        'high_is_good': type_attr.high_is_good
                    }
                )

                type_attr.display = False
                type_attr.save()

    def create_static_types(self):
        mod_to_source = defaultdict(set)

        for x in Mutator.objects.all():
            for y in x.applicable_modules.all():
                mod_to_source[x.result.id].add(y.id)

        for abyssal_id, sources in tqdm(mod_to_source.items()):
            for s in sources:
                data = ESI.request(
                    'get_universe_types_type_id',
                    type_id=s
                ).data

                module, _ = StaticModule.objects.update_or_create(
                    id=s,
                    defaults={
                        'source_id': s,
                        'type_id': abyssal_id
                    }
                )

                for attr in data['dogma_attributes']:
                    try:
                        ModuleAttribute.objects.update_or_create(
                            static_module=module,
                            attribute_id=attr['attribute_id'],
                            new_attribute=TypeAttribute.objects.get(
                                type_id=abyssal_id,
                                attribute_id=attr['attribute_id']
                            ),
                            defaults={
                                'value': attr['value']
                            }
                        )
                    except TypeAttribute.DoesNotExist:
                        pass

    def handle(self, *args, **options):
        print("Importing types and attributes...")
        self.import_types()
        print("Repairing bad attributes...")
        self.repair_attributes()
        print("Importing mutators...")
        self.import_mutators()
        print("Creating derived attributes...")
        self.create_derived()
        print("Importing static types...")
        self.create_static_types()
