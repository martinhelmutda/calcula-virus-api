from django.db import models

# Create your models here.

class Insumo(models.Model):
    nombre = models.CharField( max_length=120)
    descripcion = models.TextField(blank=True)
    lugar_compra = models.CharField( max_length=120)
    categoria = models.CharField( max_length=120)
    caducidad = models.DateTimeField('Fecha de Caducidad')
    cantidad = models.CharField( max_length=30 ) 
    prioridad = models.IntegerField()
    duracion_promedio = models.IntegerField()

