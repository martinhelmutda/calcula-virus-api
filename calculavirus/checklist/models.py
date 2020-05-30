from django.db import models
from calculavirus.insumos.models import Insumo
from calculavirus.customeUsers.models import CustomUsers

class Checklist(models.Model):
    lugar_compra = models.CharField( max_length=120)
    user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE,null=True)

class ChecklistInsumo(models.Model):
    insumo=models.ForeignKey(Insumo,on_delete=models.CASCADE)
    checklist=models.ForeignKey(Checklist,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUsers, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    comprado = models.BooleanField()
