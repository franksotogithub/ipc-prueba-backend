# Generated by Django 3.0.7 on 2020-06-28 20:20

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('formatos', '0009_auto_20200627_0952'),
        ('shared', '0003_auto_20200623_2147'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inventario',
            new_name='Investigador',
        ),
    ]
