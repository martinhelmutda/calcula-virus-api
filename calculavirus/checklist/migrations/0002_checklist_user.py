# Generated by Django 3.0.6 on 2020-05-29 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customeUsers', '0001_initial'),
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customeUsers.CustomUsers'),
        ),
    ]
