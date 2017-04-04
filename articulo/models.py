#!usr/local/bin
# coding: latin-1

from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from storages.backends.dropbox import DropBoxStorage



class Categoria(models.Model):

    """
    Representa la categoria de los artículos.
    """

    nombre = models.CharField(max_length=30)
    filtro = models.CharField(max_length=30)
    descripcion = models.TextField()

    class Meta:
        db_table = 'categorias'
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('articulo:categoria', kwargs={'categoria': self.filtro})


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Articulo(models.Model):
    """
    Representa los articulos del blog.
    """

    titulo = models.CharField(max_length=120)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    imagen = models.ImageField(
        storage=DropBoxStorage(),
        null=True,
        blank=True,
    )
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, default=1)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    class Meta:
        db_table = 'articulos'
        ordering = ['-fecha_publicacion']
        permissions = [
            ('es_autor', 'es autor'),
        ]

    def get_introduccion(self):
        n = 200
        introduccion = ""
        for i in range(n):
            try:
                introduccion += self.contenido[i]
            except IndexError:
                break
        introduccion += " [...]"

        return introduccion

    def get_absolute_url(self):
        return reverse('articulo:ver_articulo', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.titulo

"""
    def generar_slug(self):

        original_slug = slugify(self.titulo)

        exists = Articulo.objects.filter(slug=original_slug).exists()

        if exists and (not original_slug == self.slug):
            new_slug = "%s-%d" % (original_slug, self.id)
            self.slug = new_slug
            return

        self.slug = original_slug
"""
"""
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.generar_slug()
        update_fields['slug'] = self.slug
        print update_fields
        super(Articulo, self).save(update_fields=update_fields)
"""




def create_slug(instance, new_slug=None):
    slug = slugify(instance.titulo)
    if new_slug is not None:
        slug = new_slug
    qs = Articulo.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Articulo)