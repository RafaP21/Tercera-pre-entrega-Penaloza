from django.shortcuts import render
from .models import *

def empleado (erq, nombre,cargo, sueldo):
    empleado= Empleado(nombre = nombre, cargo = cargo , sueldo = sueldo)
    empleado.save()

    
def cliente (req, nombre, producto,dni):
    cliente = Cliente(nombre = nombre, producto = producto , dni = dni)
    cliente.save()


def stock (req, nombre, cantidad, precio):
    stock = Stock (nombre= nombre, cantidad = cantidad, precio = precio)
    stock.save()