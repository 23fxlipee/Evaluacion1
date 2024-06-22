from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

class Registro (models.Model):
        correo = models.CharField(max_length=200)
        password = models.CharField(max_length=20)
        confirmar_pass= models.CharField(max_length=20)
        aceptar_terminos=models.BooleanField(default=False)


