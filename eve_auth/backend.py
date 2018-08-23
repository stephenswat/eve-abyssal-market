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
            user = EveUser.objects.get(character_id=info['CharacterID'])
        except EveUser.DoesNotExist:
            user = EveUser(character_id=info['CharacterID'])

        user.name = info['CharacterName']
        user.scope_read_contracts = SCOPE_NAMES['read_contracts'] in scopes
        user.scope_read_assets = SCOPE_NAMES['read_assets'] in scopes
        user.scope_open_window = SCOPE_NAMES['open_window'] in scopes

        user.tokens = tokens

        user.save()

        return user

    def get_user(self, user_id):
        try:
            return EveUser.objects.get(pk=user_id)
        except EveUser.DoesNotExist:
            return None
