# Generated by Django 5.0 on 2023-12-23 02:52

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product-image/')),
                ('title', models.CharField(max_length=255)),
                ('keywords', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255, null=True, populate_from='title', unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.CharField(max_length=255)),
                ('product_detail', models.TextField(blank=True, null=True)),
                ('product_totel_stoke', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_reference_sub_category', to='category.category')),
            ],
            options={
                'verbose_name_plural': 'Product',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='Images-product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]