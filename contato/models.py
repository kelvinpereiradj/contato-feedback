
from django.db import models
from django.contrib.auth.models import User

list_display = [
	'contato_autor',
	'contato_assunto',
	'contato_mensagem',
	'contato_mensagem_envio'
]


class Contato(models.Model):
	contato_autor = models.CharField(
		verbose_name="Nome:",
		help_text="Opcional",
		max_length=100,
		blank = True,)
	contato_assunto = models.CharField(
		verbose_name="Assunto:",
		help_text="Opcional",
		max_length=100,
		blank = True,
        null = True,)
	contato_mensagem = models.TextField(
		verbose_name="Sua mensagem:",
		help_text="Escreva aqui sua mensagem",
		max_length=2000,)
	contato_mensagem_envio = models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.contato_autor)




