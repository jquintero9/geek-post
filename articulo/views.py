#!usr/local/bin
# coding: latin-1

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, PermissionDenied
from .models import Articulo
from .forms import ArticuloForm


class ListaArticulos(ListView):
    """
    Esta clase mustra la lista de posts.
    """

    model = Articulo
    template_name = 'articulos/lista_articulos.html'
    context_object_name = 'lista_articulos'

    def get_context_data(self, **kwargs):
        """
        Obtiene el contenido del contexto que será enviado a la vista.
        Se sobrecarga este método para agregar contenido al contexto de la vista.
        :param kwargs: kwargs del request.
        :return: El contexto que será enviado a la vista o template.
        """
        context = super(ListaArticulos, self).get_context_data(**kwargs)
        context['admin'] = 'jhjaquintero@gmail.com'

        return context


class VerArticulo(LoginRequiredMixin, DetailView):
    model = Articulo
    template_name = 'articulos/ver_articulo.html'
    context_object_name = 'articulo'
    login_url = reverse_lazy('account_login')


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

