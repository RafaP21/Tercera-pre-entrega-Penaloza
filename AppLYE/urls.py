from django.urls import path
from AppLYE.views import *

urlpatterns = [
 path('', inicio, name = "inicio") ,
 path('cliente/', cliente, name = "cliente") ,
 path('empleado/', empleado, name = "empleado") ,
 path('stock/', stock, name = "stock") ,
 path('lista_stock/', lista_stock, name = "lista_stock") ,

]
