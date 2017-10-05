# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Gasto, Tipo_Gasto
from django.core.urlresolvers import reverse_lazy

class GastoList(ListView):
	model = Gasto

class GastoDetail(DetailView):
	model = Gasto

class GastoCreate(CreateView):
	model = Gasto
	success_url = reverse_lazy('gasto:lista')
	fields = ['fecha','gasto','descripcion','valor','sucursal'] 

class GastoUpdate(UpdateView):
	model = Gasto
	success_url = reverse_lazy('gasto:lista')
	fields = ['fecha','gasto','descripcion','valor','sucursal'] 

class GastoDelete(DeleteView):
	model = Gasto
	success_url = reverse_lazy('gasto:lista')	