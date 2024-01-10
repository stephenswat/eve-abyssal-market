from django.db import transaction

from eve_sde.models import InvType
from eve_sde.command import SDECommand, SDE_BASE


INVTYPES_URL = SDE_BASE + "invTypes.csv.bz2"


class Command(SDECommand):
    help = "Downloads inventory data from Fuzzworks."

    def _create_invtypes_helper(self, x):
        InvType.objects.update_or_create(
            id=int(x["typeID"]),
            defaults={
                "group_id": int(x["groupID"]),
                "name": x["typeName"],
            },
        )

    @transaction.atomic()
    def create_invtypes(self):
        self._create_helper(
            INVTYPES_URL, "inventory types", self._create_invtypes_helper, total=33735
        )

    def handle(self, *args, **options):
        self.create_invtypes()
