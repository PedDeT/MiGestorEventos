from django.db import models
from django.utils import timezone

# Create your models here.

# Tabla para organizadores
class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    f_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# Tabla para Eventos
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)
    f_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre