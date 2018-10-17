from django.db import transaction

from eve_sde.models import Region, Constellation, SolarSystem
from eve_sde.command import SDECommand, SDE_BASE


SOLARSYSTEMS_URL = SDE_BASE + 'mapSolarSystems.csv.bz2'
STARGATES_URL = SDE_BASE + 'mapSolarSystemJumps.csv.bz2'
REGIONS_URL = SDE_BASE + 'mapRegions.csv.bz2'
CONSTELLATIONS_URL = SDE_BASE + 'mapConstellations.csv.bz2'


class Command(SDECommand):
    help = 'Downloads map data from Fuzzworks.'

    def _create_regions_helper(self, x):
        regionId = int(x['regionID'])
        Region.objects.update_or_create(
            id=regionId,
            defaults={
                'name': x['regionName'],
            },
        )

    def _create_constellations_helper(self, x):
        Constellation.objects.update_or_create(
            id=int(x['constellationID']),
            defaults={
                'name': x['constellationName'],
                'region_id': int(x['regionID'])
            }
        )

    def _create_systems_helper(self, x):
        SolarSystem.objects.update_or_create(
            id=int(x['solarSystemID']),
            defaults={
                'name': x['solarSystemName'],
                'constellation_id': int(x['constellationID']),
            }
        )

    def _create_stargate_helper(self, x):
        ssid = int(x['fromSolarSystemID'])
        if self.last_system is None or self.last_system.id != ssid:
            self.last_system = SolarSystem.objects.get(id=ssid)

        self.last_system.gates.add(int(x['toSolarSystemID']))


    @transaction.atomic()
    def create_regions(self):
        self._create_helper(
            REGIONS_URL,
            'regions',
            self._create_regions_helper,
            total=100
        )

    @transaction.atomic()
    def create_constellations(self):
        self._create_helper(
            CONSTELLATIONS_URL,
            'constellations',
            self._create_constellations_helper,
            total=1120
        )

    @transaction.atomic()
    def create_systems(self):
        self._create_helper(
            SOLARSYSTEMS_URL,
            'systems',
            self._create_systems_helper,
            total=8035
        )

    @transaction.atomic()
    def create_gates(self):
        self.last_system = None
        self._create_helper(
            STARGATES_URL,
            'stargates', self._create_stargate_helper, total=13826)

    def handle(self, *args, **options):
        self.create_regions()
        self.create_constellations()
        self.create_systems()
        self.create_gates()
