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


from meusite.settings import *
from operator import itemgetter
from json2html import *
from django.http import QueryDict
from django.shortcuts import render
from django.http import JsonResponse
from .forms import *
from django.views import View



def contatoview(request):
	if request.method == 'POST':
		form = ContatoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contato/enviado')
		
	else:
		form = ContatoForm()
	return render(request, 'contato/contato.html', {'form': form})


def contatoenviadoview(request):
	if request.method == 'POST':	
		form = ContatoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contato/enviado')
	else:
		form = ContatoForm()
	return render(request, 'contato/contato.html', {'form': form,'mensagem':'enviado'})