# Generated by Django 3.0.6 on 2020-05-23 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customeUsers', '0001_initial'),
        ('insumos', '0003_auto_20200520_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='insumo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customeUsers.CustomUsers'),
            preserve_default=False,
        ),
    ]
