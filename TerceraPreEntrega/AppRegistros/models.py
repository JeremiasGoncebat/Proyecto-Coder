from django.db import models

# Create your models here.

class Cliente(models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono=models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: {self.telefono}"


class Vendedor(models.Model):
    razon_social=models.CharField(max_length=30)
    cuit=models.IntegerField()
    telefono = models.IntegerField()
    def __str__(self):
        return f"Razon social: {self.razon_social} - cuit: {self.cuit} - Telefono: {self.telefono}"

class Articulos(models.Model):
    nombre= models.CharField(max_length=30)
    precio=models.FloatField()
    rubro= models.CharField(max_length=30)