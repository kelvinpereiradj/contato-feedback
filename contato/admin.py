
from django.contrib import admin
from .models import *


class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    list_display = list_display
    ordering = ['contato_mensagem_envio']
    actions = []
    search_fields = list_display
    list_per_page = 500
admin.site.register(Contato, ContatoAdmin)



class UsuarioMensagensAdmin(admin.ModelAdmin):
    model = UsuarioMensagens
    list_display = usuario_mensagens_list_display
    ordering = ['pk']
    actions = []
    search_fields = list_display
    list_per_page = 500
admin.site.register(UsuarioMensagens, UsuarioMensagensAdmin)