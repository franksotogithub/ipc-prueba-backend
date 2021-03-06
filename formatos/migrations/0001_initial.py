# Generated by Django 3.0.7 on 2020-06-19 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mercado',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('hora_ini', models.CharField(blank=True, max_length=10, null=True)),
                ('n_dia', models.CharField(blank=True, max_length=1, null=True)),
                ('n_semana', models.CharField(blank=True, max_length=1, null=True)),
                ('mes', models.CharField(blank=True, max_length=2, null=True)),
                ('anio', models.CharField(blank=True, max_length=4, null=True)),
                ('cod_inv_precios', models.CharField(blank=True, max_length=4, null=True)),
                ('hora_fin', models.CharField(blank=True, max_length=10, null=True)),
                ('id_prod', models.CharField(blank=True, max_length=50, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('peso', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('id_ce', models.CharField(blank=True, max_length=1, null=True)),
                ('id_cc', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
    ]
