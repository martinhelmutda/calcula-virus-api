# Generated by Django 3.0.6 on 2020-05-21 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insumos', '0003_auto_20200520_0112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lugarcompra',
            old_name='img',
            new_name='image',
        ),
    ]
