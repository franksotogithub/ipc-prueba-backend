# Generated by Django 3.0.7 on 2020-06-27 14:52

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('formatos', '0008_remove_movmercadocab_ciudad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movmercadocab',
            old_name='inv_id',
            new_name='inv',
        ),
        migrations.RenameField(
            model_name='movmercadocab',
            old_name='mercado_id',
            new_name='mercado',
        ),
        migrations.RenameField(
            model_name='movmercadodet',
            old_name='mov_mercado_cab_id',
            new_name='mov_mercado_cab',
        ),
        migrations.RenameField(
            model_name='movmercadodet',
            old_name='producto_id',
            new_name='producto',
        ),
    ]
