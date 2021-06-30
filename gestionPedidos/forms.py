from django import forms
from django.db import models
from gestionPedidos.models import Articulo

class FormularioArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = {'nombre', 'seccion', 'precio', 'descripcion', 'imagen'}