from django.shortcuts import render
from django.http import HttpResponse
from AppCursado.models import Curso
# Create your views here.

def curso(request):

      curso = Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)
