from django.http import HttpResponse
import datetime
from django.template import Template,Context
def Saludo (request):
    externo=open("I:/Saber_15/Pro/templates/Saludo.html")
    x = Template(externo.read())
    externo.close()

    ctx = Context()
    documento = x.render(ctx)
    return HttpResponse(documento)
def Fecha(request):
    fecha_ac = datetime.datetime.now()
    fecha = """<html lang="es">
    <head>
    <meta charset="UTF-8">Pro/promedios/views.py:13
    <title>Fecha</title>
    </head>
    <body>
    <h1>
    Fecha y Hora actuales: %s
    <h1>
    </body>
    </html>""" % fecha_ac
    return HttpResponse (fecha)

def CalculaEdad(request,agno):
    edadactual = 20
    periodo = agno - 2020
    edadfutura = edadactual + periodo
    fecha = "</html><body><h1>en el año %s tendras %s años" %(agno,edadfutura)
    return HttpResponse(fecha)