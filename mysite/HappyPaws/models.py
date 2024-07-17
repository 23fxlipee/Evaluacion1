from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

class Registro (models.Model):
        correo = models.CharField(max_length=200)
        password = models.CharField(max_length=20)
        confirmar_pass= models.CharField(max_length=20)
        aceptar_terminos=models.CharField(max_length=20)

class DatosPago(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    codigo_postal = models.CharField(max_length=7)

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()
    activado = models.BooleanField(default=True)

class DetalleCompra(models.Model):
    cantidad = models.IntegerField()
    subtotal = models.FloatField()
    IVA = models.FloatField()
    total = models.FloatField() 

class Pedido(models.Model):
    fecha = models.DateTimeField() 

