
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
    path(
        'admin/', 
        admin.site.urls
    ),


    path(
        'texto_dados/', 
        include(
            'texto_dados.urls', 
            namespace='texto_dados'
        )
    ),


    path(
        'administrar/', 
        include(
            'administrar.urls', 
            namespace = 'administrar'
        )
    ),

 
    path(
        '', 
        views.pagina_inicial_views, 
        name = "inicial"
    ),


    path(
        'autenticar/', 
        include(
            'autenticar.urls', 
            namespace = 'autenticar'
        )
    ),


    path(
        'accounts/', 
        include('allauth.urls')
    ),


    path(
        'artigo/', 
        include(
            'artigo03.urls', 
            namespace = 'artigo'
        )
    ),


    path(
        'jogo_ingles_portugues/', 
        include(
            'jogo_ingles_portugues.urls', 
            namespace = 'jogo'
        )
    ),


    path(
        'jogo_ingles_portugues_dados_carregar/', 
        include(
            'jogo_ingles_portugues_dados_carregar.urls', 
            namespace = 'jogo_ingles_portugues_dados_carregar'
        )
    ),
 

]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
