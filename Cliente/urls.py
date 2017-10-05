from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ClienteList.as_view(),name='lista'),
    url(r'^(?P<pk>[0-9]+)/$', views.ClienteDetail.as_view(),name='detalle'),
    url(r'^nuevo/$', views.ClienteCreate.as_view(),name='nuevo'),
    url(r'^editar/(?P<pk>[0-9]+)/$', views.ClienteUpdate.as_view(),name='editar'),
    url(r'^eliminar/(?P<pk>[0-9]+)/$', views.ClienteDelete.as_view(),name='eliminar'),

]