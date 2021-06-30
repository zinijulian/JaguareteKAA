from django.urls import path
from . import views

app_name="carro"

urlpatterns = [
    path('agregar/<int:producto_id>/', views.Agregar, name='agregar'),
    path('eliminar/<int:producto_id>/', views.Eliminar, name='eliminar'),
    path('restar/<int:producto_id>/', views.Restar, name='restar'),
    path('sumar/<int:producto_id>/', views.Sumar, name='sumar'),
    path('limpiar/', views.Limpiar, name='limpiar'),
]
