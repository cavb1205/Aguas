# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0002_auto_20170928_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_pedido',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
