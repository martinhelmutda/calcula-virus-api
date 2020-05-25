import json

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from calculavirus.insumos.serializers import GroupSerializer, InsumoSerializer, LugarCompraSerializer, UserSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
import datetime

'''
Usar un Auth Sencillo
Enviar los parámetros de registro en el Body

curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/

'''



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class InsumoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows insumos to be viewed or edited.
    """
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer
    #permission_classes = [permissions.IsAuthenticated]

    #@detail_route(methods=['post'])

    def post(self,request,pk):
        if(int(pk)>10000):
            insumo=Insumo.objects.get(pk=(int(pk)-10000))
            insumo.delete()
            return Response({"All": "OK"})
        if(int(pk)==0):
            print("Case 1")
            insumo = Insumo()
        else:
            print("Case 2")
            insumo=Insumo.objects.get(pk=pk)
        request_dict=request.data.dict()
        lugar=LugarCompra.objects.get(id=request_dict["lugar_compra"])
        insumo.nombre=request_dict["nombre"]
        insumo.marca = request_dict["marca"]
        insumo.descripcion = request_dict["descripcion"]
        insumo.lugar_compra = lugar
        insumo.categoria = request_dict["categoria"]
        insumo.caducidad = datetime.datetime(int(request_dict["caducidad_year"]),
                                             int(request_dict["caducidad_month"]),
                                             int(request_dict["caducidad_day"]))
        insumo.prioridad = request_dict["prioridad"]
        insumo.duracion_promedio = request_dict["duracion_promedio"]
        insumo.cantidad = request_dict["cantidad"]
        insumo.save()
        return Response({"All":"OK"})

    def upload_docs(self):
        try:
            file = self.request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        insumo = Insumo.objects.create(image=file)

class LugarCompraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Lugares de compra to ve viewed
    """
    queryset = LugarCompra.objects.all()
    serializer_class = LugarCompraSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def upload_docs(self):
        try:
            file = self.request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        insumo = Insumo.objects.create(img=file)