from django.shortcuts import redirect
from .carro import Carro
from django.contrib.auth.decorators import login_required
from gestionPedidos.models import Articulo

# Create your views here.

@login_required
def Agregar(request, producto_id):
    carro=Carro(request)
    producto=Articulo.objects.get(id=producto_id)
    carro.agregarProducto(producto=producto)
    return redirect("../../../productos")

def Eliminar(request, producto_id):
    carro=Carro(request)
    producto=Articulo.objects.get(id=producto_id)
    carro.eliminarProducto(producto=producto)
    return redirect("../../../carrito")

def Restar(request, producto_id):
    carro=Carro(request)
    producto=Articulo.objects.get(id=producto_id)
    carro.restarProducto(producto=producto)
    return redirect("../../../carrito")

def Sumar(request, producto_id):
    carro=Carro(request)
    producto=Articulo.objects.get(id=producto_id)
    carro.sumarProducto(producto=producto)
    return redirect("../../../carrito")

def Limpiar(request):
    carro=Carro(request)
    carro.limpiarCarro()
    return redirect("../../../carrito")