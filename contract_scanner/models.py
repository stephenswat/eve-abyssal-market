from django.db import models


class Contract(models.Model):
    id = models.IntegerField(primary_key=True)

    available = models.BooleanField(db_index=True, default=True)

    issuer_id = models.BigIntegerField(db_index=True)

    price = models.DecimalField(max_digits=32, decimal_places=2, db_index=True)

    plex = models.IntegerField(default=0)

    issued_at = models.DateTimeField()
    expires_at = models.DateTimeField()

    seen_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    single_item = models.BooleanField()
    auction = models.BooleanField()

    modules = models.ManyToManyField(
        "abyssal_modules.Module", related_name="contracts", editable=False
    )

    location_id = models.BigIntegerField(db_index=True)
    region_id = models.BigIntegerField(db_index=True)

    sold = models.BooleanField(null=True)


class PlexPriceRecord(models.Model):
    time = models.DateTimeField(db_index=True, auto_now_add=True)
    price = models.IntegerField()

    class Meta:
        get_latest_by = "time"
