from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

#Tabla para Usuarios
class CustomUser(AbstractUser):
    name = models.CharField(max_length=150)


# Tabla para Eventos
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)
    organizador = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombre