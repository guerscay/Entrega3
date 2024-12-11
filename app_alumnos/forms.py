from django import forms
from app_alumnos.models import Alumnos

class CrearAlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'apellido', 'anio_nacimiento', 'email']
        widgets = {
            'anio_nacimiento': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@mail.com'}),
        }
