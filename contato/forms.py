
from django import forms
from django.forms import ModelForm
from .models import *


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'

