"""
from django.contrib import admin
from artigos.models import *
from django import forms
from artigos.forms import *


class Artigo1Admin(admin.ModelAdmin):
    model = Artigo
    list_display = list_diplay
    ordering = ['pk']
    actions = []
    search_fields = ['artigo_titulo1']
    list_per_page = 500
    form = ArtigoForm

    

class ArtigosGrupoAdmin(admin.ModelAdmin):
    model = ArtigosGrupo
    filter_horizontal = ['artigos',]
    list_display = ['artigos_grupo_nome',]
    ordering = ['pk']
    list_per_page = 500


class ImagemAdmin(admin.ModelAdmin):
    model = Imagem
    #filter_horizontal = ['titulo']
    list_display = ['titulo','detalhes']
    ordering = ['pk']
    list_per_page = 500


admin.site.register(Artigo1, Artigo1Admin)
admin.site.register(ArtigosGrupo ,ArtigosGrupoAdmin)
admin.site.register(Imagem ,ImagemAdmin)

"""