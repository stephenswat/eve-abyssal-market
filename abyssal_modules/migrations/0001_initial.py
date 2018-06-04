# Generated by Django 2.0.5 on 2018-06-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleDogmaAttribute',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('high_is_good', models.NullBooleanField()),
                ('icon_id', models.IntegerField()),
                ('unit_str', models.CharField(max_length=16)),
                ('interesting', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ModuleType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('attributes', models.ManyToManyField(related_name='_moduletype_attributes_+', to='abyssal_modules.ModuleDogmaAttribute')),
            ],
        ),
    ]