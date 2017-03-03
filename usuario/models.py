#!usr/bin/local
# coding: latin-1

from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Email(models.Model):

    """
    Esta clase representa una tabla en la base de datos,
    y en esta se guardar�n correos y contrase�as que ser�n
    utlizados por la aplicaci�n para enviar mensajes a los usuarios.
    """

    email = models.EmailField()
    password = models.CharField(max_length=250)

"""
Se obtiene el correo y la contrase�a de la aplicaci�n.
Estos valores son asignados a la configuraci�n del correo
electr�nico de la aplicaci�n.
Posteriormente con este correo se enviar�n emails a los usuarios.
"""
try:
    email = Email.objects.get(id=1)

    settings.EMAIL_HOST_USER = email.email
    settings.EMAIL_HOST_PASSWORD = email.password
except Exception:
    pass


class KeyDropBox(models.Model):
    """
    Representa una tabla en la base de datos, donde se guardar�
    La llave secreta para acceder a la aplicaci�n de Dropbox. Esta aplicaci�n
    gestionara el almacenamiento de los archivos multimedia del sitio.
    """
    key = models.CharField(max_length=80)

    class Meta:
        db_table = 'key_dropbox'


"""
Se obtiene la llave secreta para acceder a la aplicaci�n de Dropbox.
Esta llave es asignada a la configuraci�n del proyecto.
"""
try:
    key = KeyDropBox.objects.get(id=1)
    print 'key dorpbox: ', key.key
    settings.DROPBOX_OAUTH2_TOKEN = key.key
except:
    pass


