from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(min_length=7,max_length=20)

class Registro (models.Model):
        Usuario
