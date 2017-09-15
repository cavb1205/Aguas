from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.ClienteList.as_view(),name='lista'),
    

]