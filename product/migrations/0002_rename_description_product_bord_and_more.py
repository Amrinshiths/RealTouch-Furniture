# Generated by Django 5.0 on 2023-12-23 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='bord',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='keywords',
            new_name='colorBord',
        ),
        migrations.AddField(
            model_name='product',
            name='design',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
