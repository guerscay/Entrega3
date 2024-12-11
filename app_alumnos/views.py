from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render 
from app_alumnos.models import Alumnos
import random
from app_alumnos.forms import CrearAlumnoForm


#### PAGINA DE INICIO

def home(request):
    return render(request, 'app_alumnos/home.html', {})

#### CREACION DE UN ALUMNO NUEVO

def alumno_nuevo(request):
     
    formulario = CrearAlumnoForm()
    
    if request.method == 'POST':
        formulario = CrearAlumnoForm(request.POST)   
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            
            auto = Alumnos(nombre=data.get('nombre'), 
                           apellido =data.get('apellido'), 
                           anio_nacimiento=data.get('anio_nacimiento'), 
                            email = data.get('email'))
            auto.save() 
            
            return render(request, 'app_alumnos/home.html',{})

    return render(request, 'app_alumnos/alumno_nuevo.html', {'formulario':formulario}) #mi contexto ahora es el formulario








#### BUSCAR UN ALUMNO
def alumno_buscar(request):
    
    return render(request, 'app_alumnos/alumno_buscar.html', {})