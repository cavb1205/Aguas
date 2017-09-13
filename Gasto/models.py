# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Tipo_Gasto(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre


class Gasto(models.Model):
	fecha = models.DateField(auto_now=False)
	gasto = models.ForeignKey(Tipo_Gasto,null=True)
	descripcion = models.CharField(max_length=100)