# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Cliente
from django.core.urlresolvers import reverse_lazy

def inicio(request):
	return render(request, 'Cliente/index.html',{})

class ClienteList(ListView):
	model = Cliente

class ClienteDetail(DetailView):
	model = Cliente

class ClienteCreate(CreateView):
	model = Cliente
	success_url = reverse_lazy('clientes:lista')
	fields = ['nombre','direccion','telefono','celular','email','sucursal'] 

class ClienteUpdate(UpdateView):
	model = Cliente
	success_url = reverse_lazy('clientes:lista')
	fields = ['nombre','direccion','telefono','celular','email','sucursal'] 

class ClienteDelete(DeleteView):
	model = Cliente
	success_url = reverse_lazy('clientes:lista')	