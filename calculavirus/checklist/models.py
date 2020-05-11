from django.db import models
from calculavirus.insumos.models import Insumo

class Checklist(models.Model):
    lugar_compra = models.CharField( max_length=120)

class ChecklistInsumo(models.Model):
    insumo=models.ForeignKey(Insumo,on_delete=models.CASCADE)
    checklist=models.ForeignKey(Checklist,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    comprado = models.BooleanField()
