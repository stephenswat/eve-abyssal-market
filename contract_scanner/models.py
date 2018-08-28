from django.db import models

from eve_auth.models import EveUser


class Contract(models.Model):
    id = models.IntegerField(primary_key=True)

    available = models.BooleanField(db_index=True, default=True)

    issuer_id = models.BigIntegerField(db_index=True)

    price = models.DecimalField(
        max_digits=32,
        decimal_places=2,
        db_index=True
    )

    issued_at = models.DateTimeField()
    expires_at = models.DateTimeField()

    seen_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    single_item = models.BooleanField()
    auction = models.BooleanField()

    modules = models.ManyToManyField('abyssal_modules.Module', related_name='contracts')

    location_id = models.BigIntegerField(db_index=True)
