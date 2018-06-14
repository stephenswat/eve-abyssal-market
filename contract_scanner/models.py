from django.db import models

from eve_auth.models import EveUser


class Contract(models.Model):
    STATUS_CHOICES = (
        (0, 'Available'),
        (1, 'Expired'),
        (2, 'Sold'),
        (3, 'Disappeared'),
        (4, 'Canceled'),
        (5, 'Rejected'),
        (6, 'Deleted'),
        (9, 'Unknown'),
    )

    id = models.IntegerField(primary_key=True)

    status = models.SmallIntegerField(db_index=True, choices=STATUS_CHOICES)

    issuer_id = models.BigIntegerField(db_index=True)
    owner = models.ForeignKey(
        EveUser,
        models.SET_NULL,
        db_index=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=32,
        decimal_places=2,
        db_index=True
    )

    issued_at = models.DateTimeField()
    expires_at = models.DateTimeField()

    seen_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    known = models.BooleanField(default=False)
