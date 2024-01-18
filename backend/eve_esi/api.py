from typing import List
from swagger_client.api_client import ApiClient
from swagger_client.api.universe_api import UniverseApi

def get_characters_character_id(client: ApiClient, character_id: int):
    pass

def get_universe_regions(client: ApiClient) -> List[int]:
    c = UniverseApi(client)
