from django.db import models

from eve_esi import ESI, EsiException


class EveCharacterManager(models.Manager):
    def get_or_create_by_id(self, character_id):
        try:
            return self.model.objects.get(id=character_id)
        except self.model.DoesNotExist:
            try:
                character_data = ESI.request(
                    'get_characters_character_id',
                    character_id=character_id
                ).data
                character_name = character_data['name']
            except EsiException as e:
                # Handle deleted characters.
                if e.status == 404:
                    character_name = 'DELETED CHARACTER'
                else:
                    raise
            finally:
                character, _ = EveCharacter.objects.update_or_create(
                    id=character_id,
                    defaults={
                        'name': character_name
                    }
                )
            return character


class EveCharacter(models.Model):
    objects = EveCharacterManager()

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
