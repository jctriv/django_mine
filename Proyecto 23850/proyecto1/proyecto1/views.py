from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def saludo(request):
    return HttpResponse("C'est magnifique")


def segundaVista(request):


    return HttpResponse("<br>Second")

def apellido(request, ape):

    fecha = datetime.now()
    return HttpResponse(f'El profe de Coder es {ape}')

def probandoTemplate(request):
    
    miHTML = open("C:/Users/Javier/Dropbox/Proyecto 23850/proyecto1/proyecto1/plantillas/template.html")

    plantilla = Template(miHTML.read())

    miHTML.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)