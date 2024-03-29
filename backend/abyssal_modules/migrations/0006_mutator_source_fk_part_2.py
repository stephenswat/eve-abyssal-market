# Generated by Django 2.0.9 on 2018-10-17 16:18

from django.db import migrations


def convert_mutator_source(apps, schema_editor):
    Module = apps.get_model("abyssal_modules", "Module")
    InvType = apps.get_model("eve_sde", "InvType")

    for m in Module.objects.all():
        m.mutator = InvType.objects.get(id=m.mutator_type_id)
        m.source = InvType.objects.get(id=m.source_type_id)
        m.save()


class Migration(migrations.Migration):

    dependencies = [
        ("abyssal_modules", "0005_mutator_source_fk_part_1"),
    ]

    operations = [
        migrations.RunPython(convert_mutator_source),
    ]
