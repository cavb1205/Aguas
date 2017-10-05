
from django.conf.urls import url, include
from django.contrib import admin
from Cliente import views
from Cliente.views import inicio
#from Gasto import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sucursal/', include('Sucursal.urls', namespace='sucursal')),
    url(r'^cliente/', include('Cliente.urls', namespace='clientes')),
    url(r'^gasto/', include('Gasto.urls', namespace='gasto')),
    url(r'^$', views.inicio, name='inicio'),
]
