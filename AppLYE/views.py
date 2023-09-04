from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpRequest

# def empleado (erq, nombre,cargo, sueldo):
#     empleado= Empleado(nombre = nombre, cargo = cargo , sueldo = sueldo)
#     empleado.save()

    
# def cliente (req, nombre, producto,dni):
#     cliente = Cliente(nombre = nombre, producto = producto , dni = dni)
#     cliente.save()


# def stock (req, nombre, cantidad, precio):
#     stock = Stock (nombre= nombre, cantidad = cantidad, precio = precio)
#     stock.save()

def inicio (req):
    return render(req, "inicio.html")

def empleado (req):
    return render(req, "empleado.html")

def cliente (req):
    return render(req, "cliente.html")

def stock (req):
    return render(req, "stock.html")

def lista_stock(req):
    lista = Stock.objects.all()
    return render(req, "lista_stock.html", {"lista_stock" : lista})


def buscarP(req):
    return render (req, "buscarP.html")