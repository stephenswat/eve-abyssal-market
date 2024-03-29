# Generated by Django 2.1.3 on 2018-12-01 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eve_auth", "0006_delete_all_characters"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eveuser",
            name="character_id",
            field=models.BigIntegerField(db_index=True, unique=True),
        ),
        migrations.AddField(
            model_name="eveuser",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
            preserve_default=False,
        ),
    ]
