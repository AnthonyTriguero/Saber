from django.db import models

class Alumno(models.Model):
    id = models.AutoField(primary_key = True)
    nombre= models.CharField(max_length= 200,blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    curso = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    fecha_de_creacion = models.DateField('Fecha de creacion ', auto_now=True, auto_now_add=False)

    class Meta():
        verbose_name= 'Alumno'
        verbose_name_plural= 'Alumnos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Nota(models.Model):
    id_notas = models.AutoField(primary_key=True)
    nombre_de_materia = models.CharField(max_length=200, blank=False, null=False)
    n1 = models.DecimalField(max_digits=10, decimal_places=2)
    n2 = models.DecimalField(max_digits=10, decimal_places=2)
    exa = models.DecimalField(max_digits=10, decimal_places=2)
    estudiante_id = models.ManyToManyField(Alumno)


    def __str__(self):
        return self.nombre_de_materia



class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre_de_materia = models.CharField(max_length= 200,blank = False, null= False)
    curso = models.CharField(max_length= 200,blank = False, null= False)
    profesor = models.CharField(max_length= 200,blank = False, null= False)
    estudiante_id = models.ManyToManyField(Alumno)

    def __str__(self):
        return self.nombre_de_materia

class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombre_de_profesor = models.CharField(max_length= 200,blank = False, null= False)
    apellido_de_profesor = models.CharField(max_length= 200,blank = False, null= False)
    curso = models.CharField(max_length= 200,blank = False, null= False)



class GenrGeneral(models.Model):
    idgenr_general = models.AutoField(primary_key=True)
    tipo = models.CharField('Tipo',max_length=50, blank=False, null=False)
    codigo = models.CharField('Codigo',max_length=50, blank=False, null=False)
    nombre = models.CharField('Nombre',max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Lista',
        verbose_name_plural = 'Listas',
        db_table = 'genr_general'

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    id_provincia= models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length= 20,blank=False, null=False)
    planta = models.CharField(max_length= 20,blank=False, null=False)


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region= models.CharField('ingrese la region',max_length=50, blank=False, null=False)
    temperatura = models.CharField(max_length= 20,blank=False, null=False)
    id_provinvia = models.ForeignKey(Provincia,on_delete=models.CASCADE)
    plantas =  models.CharField(max_length= 20,blank=False, null=False)



class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField('Nombre de pais',max_length=50, blank=False, null=False)
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_pais



class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length= 200,blank=False, null=False)
    id_pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE)
    edad = models.CharField(max_length= 200,blank=False, null=False,)
    foto = models.CharField(max_length= 2,blank=False, null=False,)
    correo = models.CharField(max_length= 200,blank=False, null=False,)
    id_provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE)
    sudonimo = models.CharField(max_length= 200,blank=False, null=False,)


