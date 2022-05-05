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
	responsee = HttpResponse("Cookie Set")
	responsee.set_cookie('oi', 'oioi', 300000)
	responsee.set_cookie('flamengo', 'FLAMENGO', 100000)
	try:
		r1  = request.COOKIES['flamengo'] 
		r2  = request.COOKIES['oi']
		r3 = ' '
		response = r1+r3+r2
	except:
		r1 = ''
		r2 = ''
		r3 = ''
		response = r1+r3+r2

	data = request.session.get('data', datetime.now())
	request.session['data'] = f'{data} {datetime.now()}'

	num_visits01 = request.session.get('num_visits1', 0)
	request.session['num_visits01'] = num_visits01 + 1
	num_visits02 = request.session.get_expiry_age()
	num_visits03 = request.session.get_expiry_date()
	num_visits04 = request.session.get_expire_at_browser_close()
	num_visits05 = str(request.session)
	num_visits06 = request.session.session_key
	num_visits07 = request.session.items()
	num_visits08 = request.session.keys()
	num_visits09 = request.session.get_session_cookie_age()
	num_visits10 = request.session.get_expire_at_browser_close()
	
	sessao = f'\
		<br>01: {num_visits01}    <br>02: {num_visits02}    \
		<br>03: {num_visits03}    <br>04: {num_visits04}    \
		<br>05: {num_visits05}    <br>06: {num_visits06}    \
		<br>07: {num_visits07}    <br>08: {num_visits08}    \
		<br>09: {num_visits09}    <br>10: {num_visits10}    \
		<br>response: {response}  <br>data: {data}'




	usuarios = str(
		serializers.serialize(
			'json',User.objects.all())).replace(
				'", "','"<br>"').replace(
					'"pk"','<br><br>"pk"')
	
	dados1 = (str(request.META)).replace("', '","'<br>'")
	dados2 = (str(User.objects.all().values())).replace("', '","'<br>'")
	dados3 = User._meta.get_fields(include_hidden=True)

	info = str(User.objects.filter(username = request.user).values())
	
	return render(
		request, 
		'autenticar/usuario_informacoes.html',
		{
			"dados1": dados1,
			'dados2': dados2,
			'usuarios': usuarios,
			'num_visits1': num_visits01,
			'data': data,
			'sessao': sessao,
			'info': info,
			'dados3': dados3
		}
	)
	return responsee

