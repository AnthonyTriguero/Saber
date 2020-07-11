"""promedios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
from apps.notas.views import Home,crearAlumno,notasAlumno,crearMateria,listarmateria,editarMateria,eliminarMateria,General
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notas/',include(('apps.notas.urls','notas'))),
    path('home/',Home, name ='base'),
    path('nuevo',crearAlumno,name = 'alumno_crear'),
    path('calcular',notasAlumno,name = 'notas_crear'),
    path('materia',crearMateria,name = 'materia_crear'),
    path('general/',General.as_view(), name='general')




]