# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Sucursal(models.Model):
	rut = models.CharField(max_length=9)
	nombre = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)	
	representante = models.ForeignKey(User)
	caja = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	
	def __str__(self):
		return self.nombre