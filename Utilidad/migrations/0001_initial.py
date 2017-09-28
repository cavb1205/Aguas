# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sucursal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sucursal.Sucursal')),
            ],
        ),
    ]
