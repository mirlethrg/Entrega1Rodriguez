from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render, redirect
from AppRodriguez.models import Proyectos, Experiencia , Cursos


from AppRodriguez.forms import *
 
# Create your views here.

# Vista para el HTML 

def Inicio(request):
    return render(request, "index.html")

def About(request):
    return render(request, "AppRodriguez/about.html")

def Contact(request):
    return render(request, "AppRodriguez/contact.html")

def Pricing(request):
    return render(request, "AppRodriguez/pricing.html")

def Faq(request):
    return render(request, "AppRodriguez/faq.html")

# FIN vista HTML

# Vista para Formularios

# Comienzo Formulario Proyectos
def formulario_proyecto(request):
    if request.method == 'POST':
        formulario_proyecto = CrearProyecto(request.POST)
        if formulario_proyecto.is_valid():
            data = formulario_proyecto.cleaned_data
            create_proyecto = Proyectos(nombre=data.get("nombre"), localizacion=data.get("localizacion"),fecha=data.get("fecha"))
            create_proyecto.save()
            return redirect("AppInicio")
        else:
            return redirect("AppRodriguezContact")
    contexto = {
        "formproyecto": CrearProyecto()
    }
    return render(request,"AppRodriguez/blog-home.html",contexto)
#Fin Formulario Proyectos

#Comienzo Formulario Experiencia

def formulario_experiencia(request):
    if request.method == 'POST':
        formulario_experiencia = CrearExperiencia(request.POST)
        if formulario_experiencia.is_valid():
            data = formulario_experiencia.cleaned_data
            create_experiencia = Experiencia(nombre=data.get("nombre"), fechainicio=data.get("fechainicio"),fechafin=data.get("fechafin"), descripcion=data.get("descripcion"))
            create_experiencia.save()
            return redirect("AppInicio")
        else:
            return redirect("AppRodriguezContact")
    contexto = {
        "formexperiencia": CrearExperiencia()
    }
    return render(request,"AppRodriguez/blog-post.html",contexto)

#Fin Formulario Experiencia

#Comienzo Formulario Cursos

def formulario_cursos(request):
    if request.method == 'POST':
        formulario_cursos = CrearCursos(request.POST)
        if formulario_cursos.is_valid():
            data = formulario_cursos.cleaned_data
            create_cursos = Cursos(nombre=data.get("nombre"), institucion=data.get("institucion"),fechainicio=data.get("fechainicio"), fechafin=data.get("fechafin"))
            create_cursos.save()
            return redirect("AppInicio")
        else:
            return redirect("AppRodriguezContact")
    contexto = {
        "formcursos": CrearCursos()
    }
    return render(request,"AppRodriguez/portfolio-overview.html",contexto)

#Fin Formulario Cursos

# Comienzo de Vista Experiencia
def PortFolioItem(request):
    vistaexperiencia = Experiencia.objects.all()

    contexto ={
        "verexperiencia": vistaexperiencia  
    }
    
    return render(request,"AppRodriguez/portfolio-item.html",contexto)
# FIN de vista experiencia