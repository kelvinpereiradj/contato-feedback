import os
from pathlib import Path
from decouple import config
from decouple import config, Csv
from django.core.mail import send_mail
import django_on_heroku




BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())



"""
    'rede_social.apps.RedeSocialConfig',
    'testes.apps.TestesConfig',
    'contato.apps.ContatoConfig',
"""

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',


    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',


    'administrar.apps.AdministrarConfig',
    'texto_dados.apps.TextosDadosConfig', 
    'artigo03.apps.ArtigoConfig',
    'autenticar.apps.AutenticarConfig',
    'jogo_ingles_portugues.apps.Jogo_ingles_portuguesConfig',
    'jogo_ingles_portugues_dados_carregar.apps.Jogo_ingles_portugues_dados_carregarConfig',

]


# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
# Provider specific settings


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': config('CLIENT_ID'),
            'secret': config('SECRET'),
            'key':''
        },
        'REGION': 'br',
    }
}


SOCIALACCOUNT_FORMS = {
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
    'signup': 'allauth.socialaccount.forms.SignupForm',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meu_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'meu_site/templates'),
            os.path.join(BASE_DIR, 'administrar/templates'),
            os.path.join(BASE_DIR, 'artigo03/templates'),
            os.path.join(BASE_DIR, 'texto_dados/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1



WSGI_APPLICATION = 'meu_site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




MEDIA_ROOT = os.path.join(BASE_DIR, 'midias/')
MEDIA_URL = ''

#MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'imagem')]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATIC_URL = ''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'meu_site/static'),
    os.path.join(BASE_DIR, 'administrar/static'),
    os.path.join(BASE_DIR, 'artigo03/static'),
    os.path.join(BASE_DIR, 'texto_dados/static')
] 
#[os.path.join(BASE_DIR, 'static_in_env')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_on_heroku.settings(locals())



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

