#!usr/local/bin
# coding: latin-1

from django import forms
from .models import Articulo


class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'categoria', 'imagen']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input'}),
            'contenido': forms.Textarea()
        }
