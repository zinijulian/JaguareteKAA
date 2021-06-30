from django.db import reset_queries
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils import html
from gestionPedidos.models import Articulo
from django.utils.datastructures import MultiValueDictKeyError
from .form import UserRegisterForm

#Páginas
def home(request):
    productos=Articulo.objects.all()[:3]
    more=Articulo.objects.all()[3:10]
    return render(request, "home.html", {"productos": productos, "more": more})

def productos(request):
    productos=Articulo.objects.all()
    return render(request, "productos.html", {"productos": productos})

def acercade(request):
    return render(request, "acercade.html")

def add(request):
    return render(request, "add.html")

#Busqueda de productos
def base(request):
    return render(request, "base.html")

def buscar(request):
    if request.GET["search"]:
        busqueda=request.GET["search"]
        if len(busqueda)>30:
            mensaje="Busqueda demasiado larga"
        else:    
            articulo=Articulo.objects.filter(nombre__icontains=busqueda)
            return render(request, "buscador.html", {"articulo":articulo, "query":busqueda})
    else:
        mensaje="No has introducido nada"
    return HttpResponse(mensaje)

#Formulario de contacto
def contacto(request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["zinijulian@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, "home.html")

    return render(request, "contacto.html")

#Registro
def registro(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('../')
    else:
        form = UserRegisterForm

    ctx = {'form':form}
    return render(request, "registro.html", ctx)

#Carro:
@login_required
def carrito(request):
    productos=Articulo.objects.all()
    return render(request, "carrito.html", {"productos": productos})

def factura(request):
    productos = Articulo.objects.all()
    if request.method=="POST":
        subject=request.POST["nombre"] + " " + request.POST["apellido"] + " - " + request.POST["direccion"]
        message= ""
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["zinijulian@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('../')
    return render(request, "factura.html", {"productos": productos})