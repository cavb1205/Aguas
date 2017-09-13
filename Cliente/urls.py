from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clientes/', views.clientes),
    url(r'', views.inicio),

]