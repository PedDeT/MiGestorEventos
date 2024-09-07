from django.db import models

# Create your models here.

class Organizador(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)