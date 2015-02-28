from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    turismo = models.IntegerField(default=0)
    comercio = models.IntegerField(default=0)
    turista = models.IntegerField(default=0)