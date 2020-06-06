from django.db import models
from calculavirus.insumos.models import Insumo, LugarCompra
from calculavirus.customeUsers.models import CustomUsers
from django.db.models.signals import post_save

class Checklist(models.Model):
    lugar_compra = models.CharField( max_length=120)
    user = models.CharField( max_length=120)

class ChecklistInsumo(models.Model):
    insumo=models.ForeignKey(Insumo,on_delete=models.CASCADE)
    checklist=models.ForeignKey(Checklist,on_delete=models.CASCADE)
    user = models.CharField( max_length=120)
    cantidad = models.IntegerField()
    comprado = models.BooleanField()


def create_default_checklist(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        lugar_checklist = Checklist(lugar_compra="General", user=user)
        lugar_checklist.save()


post_save.connect(create_default_checklist, sender=CustomUsers)



def create_checklist(sender, **kwargs):
    lugar = kwargs["instance"]
    if kwargs["created"]:
        lugar_checklist = Checklist(lugar_compra=lugar, user=lugar.user)
        lugar_checklist.save()


post_save.connect(create_checklist, sender=LugarCompra)
