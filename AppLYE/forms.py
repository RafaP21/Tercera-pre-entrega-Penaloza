from django import forms 

class ProductoFormulario(forms.Form):
    producto = forms.CharField(required=True)
    cantidad = forms.IntegerField(required=True)
    precio = forms.IntegerField(required=True)

class ClienteFormulario(forms.Form):
     nombre = forms.CharField(required=True)
     producto = forms.CharField(required=True)
     dni = forms.IntegerField(required=True)

class EmpleadoFormulario(forms.Form):
     nombre = forms.CharField(required=True)
     cargo = forms.IntegerField(required=True)
     sueldo = forms.IntegerField(required=True)    