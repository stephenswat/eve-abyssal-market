from eve_auth.models import EveUser


class EveAuthBackend:
    def authenticate(self, request, info=None, tokens=None):
        scopes = info['Scopes'].split(' ')

        try:
            user = EveUser.objects.get(character_id=info['CharacterID'])
        except EveUser.DoesNotExist:
            user = EveUser(character_id=info['CharacterID'])

        user.name = info['CharacterName']
        user.scope_read_contracts = 'esi-contracts.read_character_contracts.v1' in scopes
        user.scope_read_assets = 'esi-assets.read_assets.v1' in scopes
        user.scope_open_window = 'esi-ui.open_window.v1' in scopes

        user.tokens = tokens

        user.save()

        return user


    def get_user(self, user_id):
        try:
            return EveUser.objects.get(pk=user_id)
        except EveUser.DoesNotExist:
            return None
