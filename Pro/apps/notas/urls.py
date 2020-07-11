from django.urls import path,include
from .views import editarMateria,eliminarMateria,listarmateria

urlpatterns = [

    path('editarmateria/<int:id_materia>', editarMateria, name='editarMateria'),
    path('eliminar/<int:id_materia>',eliminarMateria,name = 'eliminarMateria'),
    path('listar', listarmateria, name='listarmateria'),
]