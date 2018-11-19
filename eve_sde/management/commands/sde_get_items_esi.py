from django.db import transaction

from eve_sde.models import InvType
from eve_sde.command import SDECommand, SDE_BASE

from eve_esi import ESI


class Command(SDECommand):
    help = 'Downloads inventory data from ESI.'

    @transaction.atomic()
    def create_invtypes(self):
        existing = set(InvType.objects.values_list('id', flat=True))
        available = set()

        res = ESI.head('get_universe_types')

        for p in range(1, 1 + res.header['X-Pages'][0]):
            available |= set(ESI.request('get_universe_types', page=p).data)

        to_fetch = available - existing

        for i in to_fetch:
            data = ESI.request(
                'get_universe_types_type_id',
                type_id=i
            ).data

            InvType.objects.update_or_create(
                id=i,
                defaults={
                    'group_id': data['group_id'],
                    'name': data['name'],
                }
            )

    def handle(self, *args, **options):
        self.create_invtypes()
