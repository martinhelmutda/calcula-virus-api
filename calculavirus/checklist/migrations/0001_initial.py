# Generated by Django 3.0.6 on 2020-05-09 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insumos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar_compra', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChecklistInsumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.Checklist')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.Insumo')),
            ],
        ),
    ]
