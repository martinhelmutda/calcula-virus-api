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
                ('lugar_compra', models.CharField(max_length=120)),
                ('user', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='ChecklistInsumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('comprado', models.BooleanField()),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.Checklist')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.Insumo')),
            ],
        ),
    ]
