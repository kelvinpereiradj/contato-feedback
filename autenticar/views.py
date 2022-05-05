import os
import json
import codecs
import random
from operator import itemgetter
from datetime import *

from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import View
from django.core.serializers import serialize
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.core import serializers
from django.http import QueryDict


from django.contrib.auth import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.core.cache import caches
from django.core.cache import cache
from django.template import RequestContext
from django.core.mail import send_mail



def autenticar_opcoes_view(request):
	return render(
		request, 
		'autenticar/autenticar_opcoes.html'
	)



def logar_view(request):
	AuthenticationFormx = AuthenticationForm()
	formulario = {'AuthenticationForm':AuthenticationFormx,}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate( request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/autenticar/opcoes/')
	else:
		formulario = {'AuthenticationForm': AuthenticationFormx,}
	return render(request, 'autenticar/logar.html', formulario)



def deslogar_view(request):
	logout(request)
	return HttpResponseRedirect('/autenticar/opcoes/')



def usuario_criar_view(request):
	UserCreationFormx = UserCreationForm()
	formulario = {'UserCreationForm': UserCreationFormx}
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/autenticar/logar/')
	else:
		formulario = {'UserCreationForm': UserCreationFormx}
	return render(request, 'autenticar/usuario_criar.html', formulario)



def senha_mudar_view(request):
	PasswordChangeFormx = PasswordChangeForm( user=request.user)
	formulario = {'PasswordChangeForm': PasswordChangeForm}
	if request.method == 'POST':
		form = PasswordChangeForm( user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
	else:
		formulario = {'PasswordChangeForm': PasswordChangeFormx}
	return render(request, 'autenticar/senha_mudar.html', formulario)



def senha_resetar_view(request):
	PasswordResetFormx = PasswordResetForm()
	formulario = {'PasswordResetForm': PasswordResetForm}
	if request.method == 'POST':
		form = PasswordResetForm(request.POST)
		if form.is_valid():
			form.save()
			#update_session_auth_hash(user)
	else:
		formulario = {'PasswordResetForm': PasswordResetFormx}
	return render(request, 'autenticar/senha_resetar.html', formulario)



def usuario_informacoes_view(request):

	resposta = HttpResponse("Cookie Set")
	resposta.set_cookie('set_cookie', 'set_cookie', 300000)
	try:
		response  = request.COOKIES['set_cookie'] 
	except:
		response = 'set_cookie'

	data = request.session.get('data', datetime.now())
	request.session['data'] = f'{data}<br> {datetime.now()}'
	visitas_quantidade = request.session.get('visitas_quantidade', 1)
	request.session['visitas_quantidade'] = visitas_quantidade + 1
	
	return render(
		request, 
		'autenticar/usuario_informacoes.html',
		{
			'visitas_quantidade': visitas_quantidade,
			'data': data,
		}
	)
	return resposta

