#!usr/local/bin
# coding: latin-1

from django import forms
from .models import Articulo


class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'imagen']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input'}),
            'introduccion': forms.Textarea(),
            'contenido': forms.Textarea()
        }
