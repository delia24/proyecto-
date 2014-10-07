from django.conf.urls import patterns, include.url
from view import *
from django.conf import settings
urlpatterns = patterns('',
	url(r'^$',inicio),
	url(r'^inicio1$',inicio1),
	url(r'regisusuario$',nuevoUsuario),
	url(r'^ingresar$',ingresar),
     )