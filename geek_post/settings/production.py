#!usr/local/bin
# coding: latin-1

"""
Se importa la configuraci�n de la aplicacip�n para obtener
la instancia de la base de datos que est� utilizando la aplicaci�n.
"""
from django.conf import settings
import os

"""
dj_database_url: Realiza una sincronizaci�n entre la base de datos
de la aplicaci�n y la base de datos del servidor (Heroku)
"""
import dj_database_url

"""Se desactiva el modo debug de la aplicaci�n, para que no muestre
informaci�n detallada en caso de que ocurra un error."""
DEBUG = False


DATABASES = settings.DATABASES

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

"""
Se especifica que la aplicaci�n va almacenar los archivos estaticos mediante whitenoise.
"""
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

"""
Variables necesarias para acceder al almacenamiento de Dropbox.
"""

DROPBOX_OAUTH2_TOKEN = os.environ['DROPBOX_KEY']
DROPBOX_ROOT_PATH = 'geek-post/production'

"""
Email y password desde donde la aplicaci�n enviar� correos electron�cos a los usuarios.
"""
EMAIL_HOST_USER = os.environ['EMAIL_APP']
EMAIL_HOST_PASSWORD = os.environ['PASSWORD_EMAIL_APP']
