# Generated by Django 3.1.1 on 2020-11-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201130_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='画像'),
        ),
    ]
