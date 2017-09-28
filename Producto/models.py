# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Sucursal.models import Sucursal

class Estado_Producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200,blank=True,null=True)

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	fecha_ingreso = models.DateField(auto_now_add = True)
	fecha_vencimiento = models.DateField()
	estado = models.ForeignKey(Estado_Producto)
	cantidad = models.IntegerField()
	precio = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	sucursal = models.ForeignKey(Sucursal)

	def __str__(self):
		return self.nombre