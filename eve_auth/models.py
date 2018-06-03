import datetime

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from eve_esi import get_esi_security, get_esi_client


class MyUserManager(BaseUserManager):
    def create_user(self, character_id, name):
        user = self.model(
            character_id=character_id,
            name=name,
        )

        user.save()

        return user

    def create_superuser(self, character_id, name):
        user = self.create_user(character_id, name)

        user.is_admin = True
        user.save()

        return user


class EveUser(AbstractBaseUser):
    character_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64, db_index=True, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    scope_read_contracts = models.BooleanField()
    scope_open_window = models.BooleanField()

    access_token = models.CharField(max_length=128)
    refresh_token = models.CharField(max_length=128)
    token_expiry = models.DateTimeField()

    USERNAME_FIELD = 'character_id'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def tokens(self):
        return {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'expires_in': (
                self.token_expiry -
                datetime.datetime.now(datetime.timezone.utc)
            ).total_seconds(),
            'token_type': 'Bearer',
        }

    @tokens.setter
    def tokens(self, token):
        self.access_token = token['access_token']
        self.refresh_token = token['refresh_token']
        self.token_expiry = (
            datetime.datetime.now(datetime.timezone.utc) +
            datetime.timedelta(seconds=token['expires_in'])
        )

    def get_security(self):
        res = get_esi_security()
        res.update_token(self.tokens)
        return res

    def get_client(self):
        return get_esi_client(self.get_security())

    @property
    def is_staff(self):
        return self.is_admin
