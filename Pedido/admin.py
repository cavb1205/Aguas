# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Estado_Pedido, Pedido , Detalle_Pedido
# Register your models here.

@admin.register(Estado_Pedido)
class Estado_PedidoAdmin(admin.ModelAdmin):
	pass


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
	list_display = ('fecha_pedido','cliente','fecha_entrega_pedido','estado_pedido','trabajador')


@admin.register(Detalle_Pedido)
class Detalle_PedidoAdmin(admin.ModelAdmin):
	list_display = ('id','cantidad','valor','descuento')	
