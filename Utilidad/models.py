# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Sucursal.models import Sucursal

class Utilidad(models.Model):
	fecha = models.DateField(auto_now=False)
	descripcion = models.CharField(max_length=100)
	valor = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	sucursal = models.ForeignKey(Sucursal)

