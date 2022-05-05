import os
import json
import codecs
import random
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

from PIL import Image



def pagina_inicial_views(request):
	return render(request, 'meu_site/pagina_inicial.html')

