from django.urls import path
from AppLYE.views import *

urlpatterns = [
 path('', inicio, name = "inicio") ,
 path('cliente/', cliente, name = "cliente") ,
 path('empleado/', empleado, name = "empleado") ,
 path('stock/', producto_formulario, name = "producto_formulario") ,
 path('lista_stock/', lista_stock, name = "lista_stock") ,
 path('busqueda_producto/', busquedaproducto, name = "busquedaproducto") ,
 path('buscar/', buscar, name = "buscar") ,
]
