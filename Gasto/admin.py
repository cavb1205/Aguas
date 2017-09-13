# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Gasto, Tipo_Gasto
# Register your models here.
@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
	list_display = ('gasto', 'fecha', 'descripcion')

@admin.register(Tipo_Gasto)
class Tipo_GastoAdmin(admin.ModelAdmin):
	pass