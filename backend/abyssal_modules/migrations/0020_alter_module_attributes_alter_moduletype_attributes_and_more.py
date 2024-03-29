# Generated by Django 4.0.8 on 2023-01-22 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("abyssal_modules", "0019_alter_typeattribute_high_is_good"),
    ]

    operations = [
        migrations.AlterField(
            model_name="module",
            name="attributes",
            field=models.ManyToManyField(
                related_name="+",
                through="abyssal_modules.ModuleAttribute",
                to="abyssal_modules.moduledogmaattribute",
            ),
        ),
        migrations.AlterField(
            model_name="moduletype",
            name="attributes",
            field=models.ManyToManyField(
                related_name="+",
                through="abyssal_modules.TypeAttribute",
                to="abyssal_modules.moduledogmaattribute",
            ),
        ),
        migrations.AlterField(
            model_name="staticmodule",
            name="attributes",
            field=models.ManyToManyField(
                related_name="+",
                through="abyssal_modules.ModuleAttribute",
                to="abyssal_modules.moduledogmaattribute",
            ),
        ),
    ]
