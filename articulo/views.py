#!usr/local/bin
# coding: latin-1

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, PermissionDenied
from .models import Articulo, Categoria
from .forms import ArticuloForm
from allauth.socialaccount.models import SocialAccount


class ListaArticulos(ListView):
    """
    Esta clase mustra la lista de posts.
    """
    template_name = 'articulos/lista_articulos.html'
    paginate_by = 3
    pagina_actual = None
    context_object_name = 'lista_articulos'
    model = Articulo

    def get(self, request, *args, **kwargs):
        try:
            user = SocialAccount.objects.get(user=request.user)
            print vars(request.user)
            print user.get_avatar_url()
        except:
            pass

        #print request.user.get_avatar_url()

        if 'page' in request.GET:
            self.pagina_actual = int(request.GET['page'])
        else:
            self.pagina_actual = 1

        return super(ListaArticulos, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListaArticulos, self).get_context_data(**kwargs)

        if 'categoria' in kwargs:
            categoria = kwargs['categoria']
            objeto_categoria = get_object_or_404(Categoria, filtro=categoria)
            articulos = Articulo.objects.filter(categoria=objeto_categoria.id)
            context['lista_articulos'] = articulos

        context['categorias'] = Categoria.objects.all()

        if not self.pagina_actual is None:
            context['pagina_actual'] = self.pagina_actual

        return context


class ListaArticuloCategoria(ListView):

    template_name = 'articulos/lista_articulos.html'
    paginate_by = 3
    pagina_actual = None
    context_object_name = 'lista_articulos'
    model = Articulo
    categoria = None

    def get(self, request, *args, **kwargs):
        if 'categoria' in kwargs:
            filtro= kwargs['categoria']
            self.categoria = get_object_or_404(Categoria, filtro=filtro)

        if 'page' in request.GET:
            self.pagina_actual = int(request.GET['page'])
        else:
            self.pagina_actual = 1

        return super(ListaArticuloCategoria, self).get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = super(ListaArticuloCategoria, self).get_queryset()

        if not self.categoria is None:
            queryset = Articulo.objects.filter(categoria=self.categoria.id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListaArticuloCategoria, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()

        if not self.pagina_actual is None:
            context['pagina_actual'] = self.pagina_actual

        return context


class VerArticulo(LoginRequiredMixin, DetailView):
    model = Articulo
    template_name = 'articulos/ver_articulo.html'
    context_object_name = 'articulo'
    login_url = reverse_lazy('account_login')

    def get_context_data(self, **kwargs):
        print self.kwargs
        context = super(VerArticulo, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


class CrearArticulo(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Esta clase crea un nuevo post.
    """

    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulos/crear_articulo.html'
    success_url = reverse_lazy('articulo:lista_articulos')
    login_url = reverse_lazy('account_login')
    success_message = u'El artículo %(titulo)s ha sido creado exitosamente.'

    def post(self, request, *args, **kwargs):
        id = str(request.user.id)
        request.POST['autor'] = id

        return super(CrearArticulo, self).post(request, *args, **kwargs)


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

