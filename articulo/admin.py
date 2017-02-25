from django.contrib import admin
from .models import Articulo, Categoria


class ArticuloAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'ultima_actualizacion', 'fecha_publicacion', 'categoria']
    list_display_links = ['ultima_actualizacion']
    list_editable = ['titulo']
    list_filter = ['fecha_publicacion']
    search_fields = ['titulo', 'contenido']

    class Meta:
        model = Articulo


class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'descripcion']

    class Meta:
        model = Categoria


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Categoria, CategoriaAdmin)
