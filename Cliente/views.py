# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Cliente


def inicio(request):
	return render(request, 'clientes/index.html',{})


def clientes(request):
	clientes = Cliente.objects.all()
	return render(request, 'clientes/clientes.html', {'clientes':clientes})

