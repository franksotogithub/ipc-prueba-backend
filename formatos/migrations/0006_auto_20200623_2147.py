# Generated by Django 3.0.7 on 2020-06-24 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formatos', '0005_auto_20200622_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movmercadocab',
            old_name='id_mercado',
            new_name='mercado_id',
        ),
        migrations.RenameField(
            model_name='movmercadodet',
            old_name='id_mov_mercado_cab',
            new_name='mov_mercado_cab_id',
        ),
        migrations.RenameField(
            model_name='movmercadodet',
            old_name='id_producto',
            new_name='producto_id',
        ),
    ]
