from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Articulo(models.Model):
    """
    Representa los articulos del blog.
    """

    titulo = models.CharField(max_length=120)
    introduccion = models.TextField(max_length=240)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, default=1)

    class Meta:
        db_table = 'articulos'
        ordering = ['-fecha_publicacion']
        permissions = [
            ('es_autor', 'es autor'),
        ]

    def __unicode__(self):
        return self.titulo
