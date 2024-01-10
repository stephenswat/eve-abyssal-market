# Generated by Django 2.0.5 on 2018-09-01 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("abyssal_modules", "0003_type_attributes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="moduledogmaattribute",
            name="high_is_good",
        ),
        migrations.RemoveField(
            model_name="moduledogmaattribute",
            name="interesting",
        ),
        migrations.AddField(
            model_name="typeattribute",
            name="high_is_good",
            field=models.NullBooleanField(),
        ),
    ]