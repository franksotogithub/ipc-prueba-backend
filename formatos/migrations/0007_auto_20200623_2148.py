# Generated by Django 3.0.7 on 2020-06-24 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formatos', '0006_auto_20200623_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movmercadocab',
            old_name='id_ciudad',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='movmercadocab',
            old_name='id_inv',
            new_name='inv_id',
        ),
    ]
