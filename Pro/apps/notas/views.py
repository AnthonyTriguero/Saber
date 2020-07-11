from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AlumnoForm,NotasForm,MateriasFrom
from .models import Materia,GenrGeneral
from django.views.generic import CreateView, ListView, UpdateView

def Home (request):
    return render(request,'base/base.html')

def crearAlumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('base')
    else:
        form = AlumnoForm()
    return render(request,'notas/alumno_form.html',{'form': form})


def notasAlumno(request):
    form= NotasForm(request.POST)
    if request.method == 'POST':
        v1=float(request.POST['n1'])
        v2=float(request.POST['n2'])
        v3=float(request.POST['exa'])
        resultado = v1+v2+v3
        resultado2 =resultado/3
        if form.is_valid():
            form.save()
        return HttpResponse(resultado2)
    return render(request,'notas/Notas.html',{'form':form})

def crearMateria(request):
    if request.method == 'POST':
        form = MateriasFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('base')
    else:
        form = MateriasFrom()
    return render(request,'notas/alumno_form.html',{'form': form})

def editarMateria(request,id_materia):
    materia = Materia.objects.get(id_materia= id_materia)
    if request.method == 'GET':
        form = MateriasFrom(instance= materia)
    else:
        form = MateriasFrom(request.POST, instance= materia)
        if form.is_valid():
            form.save()
        return redirect('base')
    return render(request,'notas/alumno_form.html',{'form':form})


def listarmateria(request):
    materias = Materia.objects.all()
    contexto = {'materias':materias}
    return render(request,'notas/listar_materia.html',contexto)

def eliminarMateria(request,id_materia):
    materia = Materia.objects.get(id_materia=id_materia)
    if request.method == 'POST':
        materia.delete()
        return redirect ('notas:listarmateria')
    return render(request,'notas/eliminar_materia.html',{'materia':materia})


class General(ListView):
    model = GenrGeneral
    queryset = model.objects.filter(idgenr_general=97).values('idgenr_general','codigo', 'codigo', 'nombre')
    context_object_name = 'tip'
    template_name = 'notas/prueba4.html'

