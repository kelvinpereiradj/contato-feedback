
"""
import os
from django.db import models
from django.contrib.auth.models import User
from meusite import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import urllib


artigos_pasta = FileSystemStorage(
	location=os.path.join(settings.BASE_DIR, 'templates/artigos/artigos'))
class Artigo(models.Model):
	artigo_titulo = models.CharField(
		max_length=1000,
		blank = True,
        null = True,)	
	artigo_link = models.CharField(
		max_length=1000,
		blank = True,
        null = True,)
	artigo_conteudo_escrito = models.CharField(
		max_length=1000000,
		blank = True,
        null = True,)
	artigohtml = models.FileField(
		storage = artigos_pasta,
		blank = True,
        null = True,)
	def __str__(self):
		return str(self.artigo_titulo)



class ArtigosGrupo(models.Model):
	artigos_grupo_nome = models.CharField(max_length=1000)
	artigos = models.ManyToManyField(Artigo)
	artigos_grupo_link = models.CharField(
		max_length=1000,
		blank = True,
		null = True,)
	def __str__(self):
		return str(self.artigos_grupo_nome)


class Imagem(models.Model):
	titulo = models.CharField(max_length=1000)
	detalhes =  models.CharField(max_length=10000)
	imagem = models.ImageField(upload_to='imagem')






list_diplay =[
	'artigo_titulo1',
	'artigo_link1',
	'artigo_link_acessibilidade1',
	'artigo_arquivo_html1',
	'artigo_pasta_html1',
]

artigos_pasta1 = FileSystemStorage(
	location=os.path.join(settings.BASE_DIR, 'templates/artigos/artigos'))
class Artigo1(models.Model):
	artigo_titulo1 = models.CharField(
		max_length=1000,
		blank = True,
        null = True,)	
	artigo_link1 = models.CharField(
		max_length=1000,
		blank = True,
        null = True,)
	artigo_link_acessibilidade1 = models.CharField(
		max_length=1000,
		blank = True,
        null = True,)
	artigo_pasta_html1 = models.CharField(
		max_length=1000000,
		blank = True,
        null = True,)
	artigo_arquivo_html1 = models.FileField(
		storage = artigos_pasta1,
		blank = True,
        null = True,)
	def __str__(self):
		return str(self.artigo_titulo1)

"""