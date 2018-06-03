from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


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

    USERNAME_FIELD = 'character_id'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin
