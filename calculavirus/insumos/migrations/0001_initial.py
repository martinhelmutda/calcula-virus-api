import calculavirus.insumos.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LugarCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField(blank=True)),
                ('user', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, default='location.png', max_length=254, null=True, upload_to=calculavirus.insumos.models.lugarFile)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('marca', models.CharField(max_length=120)),
                ('descripcion', models.TextField(blank=True)),
                ('user', models.CharField(max_length=120)),
                ('categoria', models.CharField(max_length=120)),
                ('caducidad', models.DateTimeField(verbose_name='Fecha de Caducidad')),
                ('cantidad', models.CharField(max_length=30)),
                ('prioridad', models.IntegerField()),
                ('duracion_promedio', models.IntegerField()),
                ('image', models.ImageField(blank=True, max_length=254, null=True, upload_to=calculavirus.insumos.models.productFile)),
                ('fecha_ultima_compra', models.DateTimeField(default=datetime.datetime.now)),
                ('lugar_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.LugarCompra')),
            ],
        ),
    ]

