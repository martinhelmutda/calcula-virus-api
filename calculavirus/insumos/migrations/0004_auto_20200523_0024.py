# Generated by Django 3.0.6 on 2020-05-23 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insumos', '0003_insumo_fecha_ultima_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='lugar_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.LugarCompra'),
        ),
    ]
