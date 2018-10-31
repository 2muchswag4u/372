from django.db import models
from datetime import datetime

class Trabajo(models.Model):
    titulo = models.CharField(max_length=200)
    detalle = models.TextField()
    categoria = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    creacion = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Trabajos'


class CategoriaTrabajo(models.Model):
    name = models.CharField(max_length=100)
    