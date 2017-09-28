# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Sucursal.models import Sucursal

class Rol_Trabajador(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre
	
class Trabajador(models.Model):
	rut = models.CharField(max_length=9)
	nombres = models.CharField(max_length=100)
	celular = models.CharField(max_length=12)
	email = models.EmailField(max_length=100)
	estado = models.BooleanField()
	rol = models.ForeignKey(Rol_Trabajador,null=True)
	sucursal = models.ForeignKey(Sucursal)

	def __str__(self):
		return self.nombres