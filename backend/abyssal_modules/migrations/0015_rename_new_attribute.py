# Generated by Django 2.1.3 on 2018-12-01 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("abyssal_modules", "0014_static_modules"),
    ]

    operations = [
        migrations.RenameField(
            model_name="moduleattribute",
            old_name="_new_attribute",
            new_name="new_attribute",
        ),
    ]
