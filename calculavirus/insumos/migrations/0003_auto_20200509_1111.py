# Generated by Django 3.0.6 on 2020-05-09 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insumos', '0002_lugarcompra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lugarcompra',
            old_name='descipcion',
            new_name='descripcion',
        ),
    ]
