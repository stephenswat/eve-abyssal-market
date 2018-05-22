from eve_auth.models import EveUser


class EveAuthBackend:
    def authenticate(self, request, character_id, name):
        user, _ = EveUser.objects.get_or_create(
            character_id=character_id,
            defaults={'name': name}
        )

        return user


    def get_user(self, user_id):
        try:
            return EveUser.objects.get(pk=user_id)
        except EveUser.DoesNotExist:
            return None
