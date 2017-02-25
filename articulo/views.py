#!usr/local/bin
# coding: latin-1

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, PermissionDenied
from .models import Articulo, Categoria
from .forms import ArticuloForm


class ListaArticulos(View):
    """
    Esta clase mustra la lista de posts.
    """
    template_name = 'articulos/lista_articulos.html'
    context = {}

    def get(self, request):
        try:
            if request.GET['categoria']:
                categoria = request.GET['categoria']
                objeto_categoria = Categoria.objects.get(nombre=categoria)
                articulos = Articulo.objects.filter(categoria=objeto_categoria.id)
        except:
            articulos = Articulo.objects.all()

        self.context['lista_articulos'] = articulos
        self.context['categorias'] = Categoria.objects.all()

        return render(request, self.template_name, self.context)


class VerArticulo(LoginRequiredMixin, DetailView):
    model = Articulo
    template_name = 'articulos/ver_articulo.html'
    context_object_name = 'articulo'
    login_url = reverse_lazy('account_login')

    def get_context_data(self, **kwargs):
        context = super(VerArticulo, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


class CrearArticulo(SuccessMessageMixin, CreateView):
    """
    Esta clase crea un nuevo post.
    """

    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulos/crear_articulo.html'
    success_url = reverse_lazy('articulo:lista_articulos')

    success_message = u'El artículo %(titulo)s ha sido creado exitosamente.'

    def get(self, request):
        if request.user.has_perm('articulo.es_autor'):
            return super(CrearArticulo, self).get(request)
        else:
            raise PermissionDenied


class EditarArticulo(SuccessMessageMixin, UpdateView):

    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulos/editar_articulo.html'
    success_url = reverse_lazy('articulo:lista_articulos')

    success_message = u'El artículo %(titulo)s ha sido editado.'


class EliminarArticulo(DeleteView):
    model = Articulo
    context_object_name = 'articulo'
    template_name = 'articulos/eliminar_articulo.html'
    success_url = reverse_lazy('articulos:lista_articulos')

