from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.SucursalList.as_view(),name='lista'),
    url(r'^(?P<pk>[0-9]+)/$', views.SucursalDetail.as_view(),name='detalle'),
    url(r'^nuevo/$', views.SucursalCreation.as_view(), name='nuevo'),
    

]