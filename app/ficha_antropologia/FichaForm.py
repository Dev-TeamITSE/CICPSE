from django import forms
from .models import Ficha

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = ['nro_id', 'nro_sigla_cicpse', 'nombre_coleccion']  # Solo los campos obligatorios
