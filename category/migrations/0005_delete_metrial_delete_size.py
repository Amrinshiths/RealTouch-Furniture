# Generated by Django 5.0 on 2023-12-26 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_alter_metrial_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Metrial',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]