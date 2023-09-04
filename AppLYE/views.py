from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpRequest
from .forms import ProductoFormulario, ClienteFormulario,EmpleadoFormulario



def inicio (req):
    return render(req, "inicio.html")




def empleado (req):
     if req.method == "POST":
        miformularioE = EmpleadoFormulario(req.POST) 

        if miformularioE.is_valid ():
            print (miformularioE.cleaned_data)
            data = miformularioE.cleaned_data
            empleado= Empleado(nombre= data["nombre"], cargo=data["cargo"] ,sueldo = data["sueldo"])
            empleado.save()
            return render (req,"inicio.html",{"mensaje" : "El Empleado a sido registrado!!"})
        else : 
            return render (req, "inicio.html", {"mensaje" : "Formulario invalido"})
     else: 
        miformularioE = EmpleadoFormulario()
        return render(req, "empleado.html", {"miformularioE": miformularioE})



def cliente (req):
  if req.method == "POST":
        miformularioc = ClienteFormulario(req.POST) 

        if miformularioc.is_valid ():
            print (miformularioc.cleaned_data)
            data = miformularioc.cleaned_data
            cliente= Cliente(nombre= data["nombre"], producto=data["producto"] ,dni = data["dni"])
            cliente.save()
            return render (req,"inicio.html",{"mensaje" : "El Cliente hizo su compra"})
        else : 
            return render (req, "inicio.html", {"mensaje" : "Formulario invalido"})
  else: 
        miformularioc = ClienteFormulario()
        return render(req, "cliente.html", {"miformularioc": miformularioc})


def lista_stock(req):
    lista = Stock.objects.all()
    return render(req, "lista_stock.html", {"lista_stock" : lista})


def buscarP(req):
    return render (req, "buscarP.html")

def producto_formulario(req :HttpRequest):
    print('method' , req.method)
    print('post', req.POST)

    if req.method == "POST":
        miformulario = ProductoFormulario(req.POST) 

        if miformulario.is_valid ():
            print (miformulario.cleaned_data)
            data = miformulario.cleaned_data
            stock= Stock(producto= data["producto"], cantidad=data["cantidad"] ,precio = data["precio"])
            stock.save()
            return render (req,"inicio.html",{"mensaje" : "Producto agregado al stock"})
        else : 
            return render (req, "inicio.html", {"mensaje" : "Formulario invalido"})
    else: 
        miformulario = ProductoFormulario()
        return render(req, "producto_formulario.html", {"miformulario": miformulario})

def busquedaproducto (req):
    return render(req,"busquedaproducto.html")

def buscar (req):
     if req.GET["producto"]:
         producto = req.GET["producto"]
         
         producto= Stock.objects.get(producto=producto)
         
         if producto : 
             
          return render(req, "resultado.html", {"producto": producto} )
         else:
             return HttpResponse("No hay en stock")
             
     else: 
         return HttpResponse("No ingresaste ningun producto")
     
    