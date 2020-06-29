# Generated by Django 3.0.7 on 2020-06-23 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('shared', '0002_inventario'),
        ('formatos', '0003_auto_20200622_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movmercadocab',
            name='id_ciudad',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='movmercadocab',
            name='id_inv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shared.Inventario'),
        ),
        migrations.AlterField(
            model_name='movmercadodet',
            name='cc',
            field=models.CharField(blank=True, choices=[(1, 'Nominal'), (2, 'Compra')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='movmercadodet',
            name='ce',
            field=models.CharField(blank=True, choices=[(1, 'Abundancia'), (2, 'Normal'), (3, 'Escacez'), (4, 'Escaces total')], max_length=1, null=True),
        ),
    ]
