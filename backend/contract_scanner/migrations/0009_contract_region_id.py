# Generated by Django 2.0.5 on 2018-09-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contract_scanner", "0008_contract_auction"),
    ]

    operations = [
        migrations.AddField(
            model_name="contract",
            name="region_id",
            field=models.BigIntegerField(db_index=True, default=0),
            preserve_default=False,
        ),
    ]
