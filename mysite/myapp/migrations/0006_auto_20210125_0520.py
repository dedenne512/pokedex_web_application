# Generated by Django 3.1.1 on 2021-01-24 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_pokemon_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predicts',
            old_name='pokemon_id',
            new_name='pokemon',
        ),
    ]