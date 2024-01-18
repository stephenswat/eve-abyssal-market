from django.db import models

from eve_esi import ESI, EsiException
import swagger_client.api.character_api

class EveCharacterManager(models.Manager):
    def get_or_create_by_id(self, character_id):
        try:
            return self.model.objects.get(id=character_id)
        except self.model.DoesNotExist:
            client = swagger_client.api.character_api.CharacterApi()
            (r, c, _) = client.get_characters_character_id_with_http_info(character_id=character_id)

            if c != 404:
                character_name = r.name
            else:
                character_name = "DELETED CHARACTER"

            character, _ = EveCharacter.objects.update_or_create(
                id=character_id, defaults={"name": character_name}
            )

            return character


class EveCharacter(models.Model):
    objects = EveCharacterManager()

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
