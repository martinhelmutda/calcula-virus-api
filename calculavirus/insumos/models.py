from django.db import models
from datetime import datetime
from calculavirus.customeUsers.models import CustomUsers

# Create your models here.

def productFile(instance, filename):
    print(str(instance.id))
    return '/'.join( ['products',filename] )

def lugarFile(instance, filename):
    print(str(instance.id))
    return '/'.join( ['lugares',filename] )


class LugarCompra(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    user = models.CharField( max_length=120)
    image = models.ImageField(
        upload_to=lugarFile,
        max_length=254, blank=True, null=True,
        default = "market.jpg"
    )

    # def __init__(self, name, creation, update, *args, **kwargs):
    #     super(LugarCompra, self).__init__(*args, **kwargs)
    #     self.name = name
    #     self.creation_datetime = creation
    #     self.update_datetime = update

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
    user = models.CharField( max_length=120)
    categoria = models.CharField( max_length=120)
    caducidad = models.DateTimeField('Fecha de Caducidad')
    cantidad = models.CharField( max_length=30 )
    prioridad = models.IntegerField()
    duracion_promedio = models.IntegerField()
    image = models.ImageField(
        upload_to=productFile,
        max_length=254, blank=True, null=True,
        default = "basket.jpg"
    )
    fecha_ultima_compra = models.DateTimeField(default=datetime.now)
