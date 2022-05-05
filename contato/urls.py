
from django.urls import path, include
from . import views


app_name = 'contato'
urlpatterns = [

	path('', views.contatoview, name="contato"),
	path('enviado', views.contatoenviadoview, name="contatoenviado")

]