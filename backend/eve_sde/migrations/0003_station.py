# Generated by Django 4.1.13 on 2024-01-10 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("eve_sde", "0002_alter_solarsystem_gates"),
    ]

    operations = [
        migrations.CreateModel(
            name="Station",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=512)),
                (
                    "inv_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="eve_sde.invtype",
                    ),
                ),
                (
                    "solar_system",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="eve_sde.solarsystem",
                    ),
                ),
            ],
        ),
    ]
