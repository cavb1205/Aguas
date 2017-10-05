from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GastoList.as_view(),name='lista'),
    url(r'^(?P<pk>[0-9]+)/$', views.GastoDetail.as_view(),name='detalle'),
    url(r'^nuevo/$', views.GastoCreate.as_view(),name='nuevo'),
    url(r'^editar/(?P<pk>[0-9]+)/$', views.GastoUpdate.as_view(),name='editar'),
    url(r'^eliminar/(?P<pk>[0-9]+)/$', views.GastoDelete.as_view(),name='eliminar'),

]