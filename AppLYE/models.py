from django.db import models

class Empleado (models.Model):
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    DNI = models.IntegerField()



class Stock (models.Model):
    producto = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

class Cliente (models.Model):
    nombre = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    DNI = models.IntegerField()
   
