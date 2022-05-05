
from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

app_name = 'autenticar'
urlpatterns = [
	path('opcoes/', views.autenticar_opcoes_view, name="autenticar_opcoes"),
	path('logar/', views.logar_view, name="logar"),
	path('deslogar/', views.deslogar_view, name="deslogar"),
	path('usuario_criar/', views.usuario_criar_view, name="usuario_criar"),
	path('senha_mudar/', views.senha_mudar_view, name="senha_mudar"),
	path('senha_resetar/', views.senha_resetar_view, name="senha_resetar"),
	path('usuario_informacoes/', views.usuario_informacoes_view, name="usuario_informacoes"),


	path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
	path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
