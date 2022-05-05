
from django.contrib import admin
from dadoscarregar.models import *
from .models import *


class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    list_display = list_display
    ordering = ['contato_mensagem_envio']
    actions = []
    search_fields = list_display
    list_per_page = 500



admin.site.register(Contato, ContatoAdmin)
