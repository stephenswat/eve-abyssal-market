# Generated by Django 2.0.5 on 2018-09-02 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("abyssal_modules", "0004_move_dogma_attributes"),
    ]

    operations = [
        migrations.CreateModel(
            name="PricePredictor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("quality", models.FloatField()),
                ("data", models.BinaryField()),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="abyssal_modules.ModuleType",
                    ),
                ),
            ],
        ),
    ]
