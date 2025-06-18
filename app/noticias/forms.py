# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'nombre', 'apellido', 'email', 'password1', 'password2', 'area']

from django import forms  # <-- Aquí está el import faltante
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'portada']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 8}),
        }