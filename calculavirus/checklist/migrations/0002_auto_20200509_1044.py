# Generated by Django 3.0.6 on 2020-05-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='lugar_compra',
            field=models.CharField(max_length=120),
        ),
    ]