# Generated by Django 3.0.6 on 2020-06-05 00:44

import calculavirus.insumos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insumos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='image',
            field=models.ImageField(blank=True, default='basket.jpg', max_length=254, null=True, upload_to=calculavirus.insumos.models.productFile),
        ),
        migrations.AlterField(
            model_name='lugarcompra',
            name='image',
            field=models.ImageField(blank=True, default='market.jpg', max_length=254, null=True, upload_to=calculavirus.insumos.models.lugarFile),
        ),
    ]
