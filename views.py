from django.shortcuts import render
from LaFamilia.models import Familiares

# Create your views here.

def template_familia(request, nombre, segundo_nombre, documento, edad, nacimiento):
    familiar = Familiares(
        nombre = nombre,
        segundo_nombre = segundo_nombre,
        documento = documento,
        edad = edad,
        nacimiento = nacimiento
        )
    familiar.save()
    return render(
        request,
        "familiares.html",
        {'familiar': familiar}
        )

def inicio(request):
    return render(
        request,
        'index.html'
        )