from django.db import models

# Create your models here.

class Organizador(models.Model):
    nombre = models.CharField(max_length=50)


    def __unicode__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField(max_length=25)
    lugar = models.CharField(max_length=75)
    organizador = models.ForeignKey(Organizador)

    def __unicode__(self):
        return self.nombre

