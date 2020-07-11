from django import forms
from .models import Alumno,Nota,Materia,GenrGeneral

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields =['nombre',
                 'apellidos',
                 'curso',
                 'email',
                 ]

        labels={
            'nombre':'Nombre',
            'apellidos':'Apellido',
            'curso':'Curso del estudiante',
            'email':'Email'
        }

        widgets = {

            'nombre': forms.TextInput(attrs={'class':'from-control'}),
            'apellidos': forms.TextInput(attrs={'class':'from-control'}),
            'curso': forms.TextInput(attrs={'class':'from-control'}),
            'email': forms.TextInput(attrs={'class':'from-control'}),


        }


class NotasForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields =['nombre_de_materia',
                 'n1',
                 'n2',
                 'exa',
                 'estudiante_id',

                 ]



class MateriasFrom(forms.ModelForm):
    class Meta:
        model = Materia
        fields =['nombre_de_materia',
                 'curso',
                 'profesor',
                 ]
        widgets = {

            'Nombre de materia': forms.TextInput(attrs={'class': 'from-control'}),
            'Curso': forms.TextInput(attrs={'class': 'from-control'}),
            'Profesor': forms.TextInput(attrs={'class': 'from-control'}),


        }

class GenrGeneral_1(forms.ModelForm):
    class Meta:
        model = GenrGeneral
        fields =['tipo',
                 'codigo',
                 'nombre',
                 ]

        labels={
            'tipo':'Tipo',
            'codigo':'Codigo',
            'nombre':'nombre_curso',
        }

        widgets = {

            'tipo': forms.TextInput(attrs={'class':'from-control'}),
            'codigo': forms.TextInput(attrs={'class':'from-control'}),
            'nombre': forms.TextInput(attrs={'class':'from-control'}),
        }