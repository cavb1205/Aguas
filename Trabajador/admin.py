# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Rol_Trabajador, Trabajador


@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
	list_display = ('rut', 'nombres', 'email', 'celular', 'estado', 'rol')


@admin.register(Rol_Trabajador)
class Rol_TrabajadorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')
