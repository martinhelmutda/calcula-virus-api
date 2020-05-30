from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

# Aquí va todo aquello que se puede pedit por HTTP GET

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id','url', 'name']

class InsumoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insumo
        fields = (
            'id',
            'nombre',
            'marca',
            'descripcion',
            'lugar_compra',
            'categoria',
            'caducidad',
            'cantidad',
            'prioridad',
            'duracion_promedio',
            'image',
            'user'
            )

class LugarCompraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LugarCompra
        fields = ['id','nombre','descripcion','image', 'user']

