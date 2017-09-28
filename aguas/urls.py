
from django.conf.urls import url, include
from django.contrib import admin
from Cliente import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sucursal/', include('Sucursal.urls', namespace='sucursal')),
    url(r'^clientes/', include('Cliente.urls', namespace='clientes')),
    url(r'', views.inicio, name='inicio'),
]
