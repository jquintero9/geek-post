from django.conf.urls import url
from .views import (
    ListaArticulos,
    CrearArticulo,
    VerArticulo,
    EditarArticulo,
    EliminarArticulo,
)

urlpatterns = [
    url(r'^$', ListaArticulos.as_view(), name='lista_articulos'),
    url(r'^crear$', CrearArticulo.as_view(), name='crear_articulo'),
    url(r'^(?P<pk>\d+)/ver$', VerArticulo.as_view(), name='ver_articulo'),
    url(r'^(?P<pk>\d+)/editar$', EditarArticulo.as_view(), name='editar_articulo'),
    url(r'^(?P<pk>\d+)/eliminar$', EliminarArticulo.as_view(), name='eliminar_articulo'),
]
