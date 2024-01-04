# Generated by Django 5.0 on 2023-12-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morefeature', '0003_delete_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone_no', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
