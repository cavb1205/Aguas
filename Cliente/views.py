# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
from .models import Cliente


def inicio(request):
	return render(request, 'Cliente/index.html',{})

#esta forma tambien es lo mismo
'''def clientes(request):
	clientes = Cliente.objects.all()
	return render(request, 'clientes/clientes.html', {'clientes':clientes})
'''
#otra forma de mostrar una lista de un modelo 
class ClienteList(ListView):
	model = Cliente