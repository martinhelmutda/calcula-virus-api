from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Checklist
        fields = ['id','lugar_compra','user','user_id']
        user_id = serializers.SerializerMethodField('get_user_id')

        def get_user_id(self, obj):
            return obj.user.id


class ChecklistInsumoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChecklistInsumo
        fields = ['id','checklist','checklist_id','insumo','insumo_id','insumo_nombre','cantidad', 'comprado', 'usuario_nombre', 'user']

    checklist_id = serializers.SerializerMethodField('get_checklist_id')

    def get_checklist_id(self,obj):
        return obj.checklist.id

    insumo_nombre = serializers.SerializerMethodField('get_insumo_nombre')

    def get_insumo_nombre(self,obj):
        return obj.insumo.nombre

    insumo_id = serializers.SerializerMethodField('get_insumo_id')

    def get_insumo_id(self,obj):
        return obj.insumo.id

    usuario_nombre = serializers.SerializerMethodField('get_usuario_nombre')

    def get_usuario_nombre(self, obj):
        return obj.user.name
