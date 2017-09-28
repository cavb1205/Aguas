# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Producto, Estado_Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre','fecha_ingreso','fecha_vencimiento','cantidad','precio')


@admin.register(Estado_Producto)
class Estado_Producto(admin.ModelAdmin):
	pass