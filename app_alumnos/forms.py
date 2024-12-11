from django import forms
from app_alumnos.models import Alumnos

# class CrearAlumnoForm(forms.ModelForm):
#     class Meta:
#         model = Alumnos
#         fields = ['nombre', 'apellido', 'anio_nacimiento', 'email']
#         widgets = {
#             'anio_nacimiento': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
#             'email': forms.EmailInput(attrs={'placeholder': 'example@mail.com'}),
#         }

class CrearAlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}))
    apellido = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Tu apellido'}))
    anio_nacimiento = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '2000'}))
    email = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'ejemplo@email.com'}))
    