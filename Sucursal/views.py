# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import render
from .models import Sucursal
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class SucursalList(ListView):
	model = Sucursal


class SucursalDetail(DetailView):
	model = Sucursal


class SucursalCreation(CreateView):
	model = Sucursal
	success_url = reverse_lazy('sucursal:lista')
	fields = ['rut','nombre','direccion','representante','caja']	