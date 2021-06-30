from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def homepage(request):
    return render(request, "main/inicio.html", {"cursos": Curso.objects.all})

def contacto(request):
    return render(request, "main/contacto.html")    

def galeria(request):
    return render(request, "main/galeria.html")    