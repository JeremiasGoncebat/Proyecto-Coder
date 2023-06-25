from django.http import HttpResponse
from django.template import loader

def inicio(request):
    loader.get_template("Index.html")

def alumnos(request):
    loader.get_template("Alumnos.html")

def cursos(request):
    loader.get_template("Cursos.html")

def profesores(request):
    loader.get_template("Entregas.html")

def entregas(request):
    loader.get_template("Profesores.html")