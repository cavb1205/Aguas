# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Utilidad 

@admin.register(Utilidad)
class UtilidadAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'descripcion')

