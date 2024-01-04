# Generated by Django 5.0 on 2023-12-25 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_metrial_size'),
        ('product', '0003_rename_design_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('None', 'None'), ('Size', 'Size'), ('Metrial', 'Metrial')], default='None', max_length=10),
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('image_id', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.metrial')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.size')),
            ],
        ),
    ]