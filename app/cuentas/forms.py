from django import forms  
from .models import CustomUser

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'nombre', 'apellido', 'email', 'password', 'area']