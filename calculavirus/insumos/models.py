from django.db import models
from datetime import datetime
from calculavirus.customeUsers.models import CustomUsers

# Create your models here.

def productFile(instance, filename):
    return '/'.join( ['products', str(instance.id), filename] )


class LugarCompra(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    img = models.ImageField(
        upload_to=productFile,
        max_length=254, blank=True, null=True,
        default = 0
    )

    def __str__(self):
        return "%s" % self.nombre

class Insumo(models.Model):
    nombre = models.CharField( max_length=120)
    marca = models.CharField( max_length=120)
    descripcion = models.TextField(blank=True)
    lugar_compra = models.ForeignKey(
        LugarCompra,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey( CustomUsers, on_delete = models.CASCADE)
    categoria = models.CharField( max_length=120)
    caducidad = models.DateTimeField('Fecha de Caducidad')
    cantidad = models.CharField( max_length=30 )
    prioridad = models.IntegerField()
    duracion_promedio = models.IntegerField()
    image = models.ImageField(
        upload_to=productFile,
        max_length=254, blank=True, null=True
    )
    fecha_ultima_compra = models.DateTimeField(default=datetime.now)
