from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^type$', views.typeca, name='settype'),
    url(r'^create_conf$', views.create, name='create'),

]