from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import FormularioArticulo
from gestionPedidos.models import Articulo

# Create your views here.
class FormularioArticuloView():

    def index(request):
        if request.method=="POST":
            form = FormularioArticulo(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('../add')
        else:
            form = FormularioArticulo()

        ctx = {'form':form}
        return render(request, "add.html", ctx)

    def editar(request, producto_id):
        articulo = Articulo.objects.filter(id=producto_id).first()
        form = FormularioArticulo(instance=articulo)
        return render(request, "editar.html", {'form':form,'articulo':articulo})

    def actualizar(request, producto_id):
        if request.method=="POST":
            articulo = Articulo.objects.get(pk=producto_id)
            form = FormularioArticulo(request.POST, request.FILES, instance=articulo)
            if form.is_valid():
                form.save()
                return redirect('../../../productos')
        else:
            form = FormularioArticulo()
            
        return render(request, "editar.html", {'form':form,'articulo':articulo})
        
    def eliminar(request, producto_id):
        articulo = Articulo.objects.get(pk=producto_id)
        articulo.delete()
        return redirect("../../../productos")