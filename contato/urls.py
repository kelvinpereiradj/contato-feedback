
from django.urls import path, include
from . import views


app_name = 'contato'
urlpatterns = [

	path('opcoes/', views.contato_opcoes_view, name="opcoes"),
	path('', views.contato_view, name="contato"),
	path('enviado/', views.contato_enviado_view, name="contato_enviado"),
	path('nao_enviado/', views.contato_nao_enviado_view, name="contato_nao_enviado")

]