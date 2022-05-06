import os
import json
import codecs
from datetime import datetime

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
from .models import *
from .forms import *
import random


from meu_site.settings import *
from operator import itemgetter
from json2html import *
from django.http import QueryDict
from django.shortcuts import render
from django.http import JsonResponse
from .forms import *
from .models import *
from django.views import View






def usuario_mensagem(request):		
	modelo = Contato(
		contato_autor = request.POST['contato_autor'],
		contato_assunto = request.POST['contato_assunto'],
		contato_mensagem = request.POST['contato_mensagem'],
	)
	modelo.save()
	mensagem = Contato.objects.get(pk = modelo.pk)
	obj, created = UsuarioMensagens.objects.get_or_create(
		usuario = request.user
	)
	obj.usuario_mensagens.add(mensagem)	



def contato_opcoes_view(request):
	return render(request, 'contato/contato_opcoes.html')



def contato_view(request):
	if request.method == 'POST':
		form = ContatoForm(request.POST)
		if form.is_valid():
			usuario_mensagem(request)
			return HttpResponseRedirect('/contato/enviado/')
		else:
			return HttpResponseRedirect('/contato/nao_enviado/')		
	else:
		form = ContatoForm()
	return render(request, 'contato/contato.html', {'form': form})



def contato_enviado_view(request):
	if request.method == 'POST':	
		form = ContatoForm(request.POST)
		if form.is_valid():
			usuario_mensagem(request)
			return HttpResponseRedirect('/contato/enviado')
		else:
			return HttpResponseRedirect('/contato/nao_enviado/')
	else:	
		form = ContatoForm()
	return render(
		request, 
		'contato/contato.html', 
		{'form': form,'mensagem':'enviado'}
	)



def contato_nao_enviado_view(request):
	if request.method == 'POST':	
		form = ContatoForm(request.POST)
		if form.is_valid():
			usuario_mensagem(request)
			return HttpResponseRedirect('/contato/enviado')
		else:
			return HttpResponseRedirect('/contato/nao_enviado/')
	else:
		form = ContatoForm()
	return render(
		request, 
		'contato/contato.html', 
		{'form': form,'mensagem':'não enviado'}
	)