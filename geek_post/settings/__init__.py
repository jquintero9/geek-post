#!usr/local/bin
# coding: latin-1

'''
Dependiendo el entorno en que se este ejecutando la aplicaci�n,
se importar� la configuraci�n necesaria.
'''

from .base import *

try:
    from .local import *
    live = False
except:
    live = True

if live:
    from .production import *
