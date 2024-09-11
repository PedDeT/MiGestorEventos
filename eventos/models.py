from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Tabla para Eventos
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)
    organizador = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombre