from django.http import HttpResponse
import datetime 
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Segunda Vista")

def diaDeHoy(request):
    dia= datetime.datetime.now()
    documentoDeTexto=f"Hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self,nombre):
    documentoTexto=f"Mi nombre es:<br><br> {nombre}"
    return HttpResponse(documentoTexto)

def probandoTemplate(self):
    miHtml=open("C:/Users/harol/Desktop/Curso Python/Ejecicios/semana 9/Django/HolaDjango/plantillas/index.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto=Context() 
    documento=plantilla.render(miContexto)
    return HttpResponse(documento)