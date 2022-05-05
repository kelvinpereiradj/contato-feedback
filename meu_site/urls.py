
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import *
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from . import views

"""
	path('testes/', include('testes.teste01.urls')),  
  
"""

urlpatterns = [ 
    path('', views.pagina_inicial_views, name = "inicial"),
    path('admin/', admin.site.urls),
    path('autenticar/', include('autenticar.urls', namespace='autenticar')),
    path('contato/', include('contato.urls', namespace = 'contato')),

]

