# Generated by Django 2.0.5 on 2018-06-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eve_auth", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="eveuser",
            name="scope_open_window",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="eveuser",
            name="scope_read_contracts",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
