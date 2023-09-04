from django.urls import path
from AppLYE.views import *

urlpatterns = [
 path('', inicio) ,
 path('cliente/', cliente) ,
 path('empleado/', empleado) ,
 path('stock/', stock) ,
 path('lista_stock/', lista_stock) ,

]
