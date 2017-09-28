# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Cliente.models import Cliente
from Producto.models import Producto
from Trabajador.models import Trabajador

class Estado_Pedido(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre


class Pedido(models.Model):
	fecha_pedido = models.DateTimeField(auto_now_add=True)
	cliente = models.ForeignKey(Cliente)
	fecha_entrega_pedido = models.DateTimeField()
	estado_pedido = models.ForeignKey(Estado_Pedido,default=1)
	trabajador = models.ForeignKey(Trabajador)

	def __str__(self):
		return self.cliente.nombre

class Detalle_Pedido(models.Model):
	pedido = models.ForeignKey(Pedido)
	producto = models.ForeignKey(Producto)
	valor = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	cantidad = models.IntegerField(default='0')
	descuento = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

	def get_valor(self):
		return ((self.producto.precio * self.cantidad) - self.descuento)