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
            name='Estado_Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.Estado_Producto')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sucursal.Sucursal')),
            ],
        ),
    ]
