from django.contrib.auth.models import User

from eve_auth.models import EveUser


SCOPE_NAMES = {
    'read_contracts': 'esi-contracts.read_character_contracts.v1',
    'read_assets': 'esi-assets.read_assets.v1',
    'open_window': 'esi-ui.open_window.v1',
}


class EveAuthBackend:
    def authenticate(self, request, info=None, tokens=None):
        scopes = info['Scopes'].split(' ')

        try:
            character = EveUser.objects.get(character_id=info['CharacterID'])
        except EveUser.DoesNotExist:
            character = EveUser(character_id=info['CharacterID'])
            user = User.objects.create_user(info['CharacterName'])
            character.owner = user

        character.name = info['CharacterName']
        character.scope_read_contracts = SCOPE_NAMES['read_contracts'] in scopes
        character.scope_read_assets = SCOPE_NAMES['read_assets'] in scopes
        character.scope_open_window = SCOPE_NAMES['open_window'] in scopes

        character.tokens = tokens

        character.save()

        return character.owner

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except EveUser.DoesNotExist:
            return None
