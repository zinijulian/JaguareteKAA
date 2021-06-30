from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30) #tipo teto
    direccion=models.CharField(max_length=50) 
    email=models.EmailField() #tipo email
    telefono=models.CharField(max_length=15)

class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField() #tipo entero
    descripcion=models.CharField(max_length=250)
    imagen=models.ImageField()

class Pedido(models.Model):
    numero=models.IntegerField()
    fechas=models.DateField() #tipo fecha
    entregado=models.BooleanField() #tipo si o no