
from django import forms
from django.forms import ModelForm
from .models import *


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'


class UsuarioMensagensForm(forms.ModelForm):
    class Meta:
        model = UsuarioMensagens
        fields = '__all__'