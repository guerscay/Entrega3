from django.contrib import admin
from django.urls import path
from app_alumnos.views import alumno_nuevo, home, alumno_buscar

app_name = 'app_alumnos'

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('welcome', bienvenida), 
    path('', home, name = 'home'),
    path('alumnos/alumno_nuevo/', alumno_nuevo, name = 'alumno_nuevo'),
    path('alumnos/alumno_buscar/', alumno_buscar, name = 'alumno_buscar'),
]
