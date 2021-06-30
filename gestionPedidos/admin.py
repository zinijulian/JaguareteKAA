from django.contrib import admin
from django.contrib.admin.filters import BooleanFieldListFilter, SimpleListFilter
from django.db.models.fields import BooleanField
from gestionPedidos.models import Cliente, Articulo, Pedido

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "email", "telefono")
    search_fields=("nombre", "email")

class FechasAdmin(admin.ModelAdmin):
    list_display=("numero", "fechas", "entregado")
    date_hierarchy=("fechas")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("nombre", "seccion")

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Articulo, ArticulosAdmin)
admin.site.register(Pedido, FechasAdmin)