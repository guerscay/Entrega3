from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render 
from app_alumnos.models import Alumnos
import random
#from inicio.forms import CrearAuto, BuscarAuto # formularios!!


#### PAGINA DE INICIO
def home(request):
    return render(request, 'app_alumnos/home.html', {})


#### CREACION DE UN ALUMNO NUEVO
def alumno_nuevo(request):
    alumno = Alumnos(
        nombre=random.choice(['Catriel', 'Paco', 'Maria', 'Nicky', 'Karol']),
        apellido=random.choice(['Lopez', 'Gonzalez', 'Martinez', 'Diaz', 'Perez']),
        email='generico@gmail.com',
        anio_nacimiento=random.choice([1980, 1990, 2000, 2010])
    )
    alumno.save()
    return render(request, 'app_alumnos/alumno_nuevo.html', {'alumno': alumno})


#### PRUEBA
def alumno_buscar(request):
    
    return render(request, 'app_alumnos/alumno_buscar.html', {})