# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Sucursal.models import Sucursal

class Cliente(models.Model):
	nombre = models.CharField(max_length = 200)
	direccion = models.CharField(max_length = 200)
	telefono = models.CharField(max_length = 12, blank = True, null = True)
	celular = models.CharField(max_length = 12)
	email = models.EmailField(max_length = 100)
	sucursal = models.ForeignKey(Sucursal)

	def __str__(self):
		return self.nombre