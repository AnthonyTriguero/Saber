from django.contrib import admin
from .models import Alumno,Nota,Materia,GenrGeneral

class Alumnos_m(admin.ModelAdmin):
    list_display=("nombre","apellidos","curso","email")
    search_fields = ["apellidos"]


class Notas_a(admin.ModelAdmin):
    list_display=("nombre_de_materia","n1","n2","exa",)
admin.site.register(Nota,Notas_a)
admin.site.register(Alumno,Alumnos_m)


class Materias_f(admin.ModelAdmin):
    list_display=("nombre_de_materia", "curso", "profesor",)
    search_fields = ["profesor"]
admin.site.register(Materia, Materias_f)


class gene_a(admin.ModelAdmin):
    list_display = ("tipo", "codigo", "nombre",)
    search_fields = ["tipo"]
admin.site.register(GenrGeneral,gene_a)
