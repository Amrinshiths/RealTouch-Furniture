# Generated by Django 5.0 on 2023-12-23 03:14

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='hero-image/')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, max_length=255, null=True, populate_from='discription', unique=True)),
                ('discription', models.TextField(blank=True, null=True)),
                ('text', models.CharField(blank=True, max_length=300, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slider-image/')),
                ('subtitle', models.CharField(max_length=200)),
                ('header1', models.CharField(max_length=300)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, max_length=255, null=True, populate_from='subtitle', unique=True)),
                ('header2', models.CharField(max_length=300)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]