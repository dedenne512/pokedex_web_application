# Generated by Django 3.1.1 on 2020-12-07 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201130_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='画像'),
        ),
    ]
