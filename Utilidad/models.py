# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Utilidad(models.Model):
	fecha = models.DateField(auto_now=False)
	descripcion = models.CharField(max_length=100)

