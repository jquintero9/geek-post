from django.contrib import admin
from .models import Articulo


class ArticuloAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'ultima_actualizacion', 'fecha_publicacion']
    list_display_links = ['ultima_actualizacion']
    list_editable = ['titulo']
    list_filter = ['fecha_publicacion']
    search_fields = ['titulo', 'contenido']

    class Meta:
        model = Articulo


admin.site.register(Articulo, ArticuloAdmin)

