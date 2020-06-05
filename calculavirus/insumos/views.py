import json

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, mixins,generics
from calculavirus.insumos.serializers import GroupSerializer, InsumoSerializer, LugarCompraSerializer, UserSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from django.http.multipartparser import MultiPartParser
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.decorators import action
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

    @action(detail=False)
    def get_insumos_by_user(self,request):
        user_email=request.GET['user_email']
        user = CustomUsers.objects.get(email=user_email)
        insumos = Insumo.objects.filter(user=user)
        serializer_context = {
            'request': request,
        }
        serializer =  InsumoSerializer(insumos,many=True,context=serializer_context)
        return Response({'count':insumos.count(),'next':None,'previous':None,'results':serializer.data})

    @action(detail=False)
    def get_insumo_by_priority(self,request):
        user_email=request.GET['user_email']
        user = CustomUsers.objects.get(email=user_email)
        insumos = Insumo.objects.filter(user=user).order_by('prioridad')
        serializer_context = {
            'request': request,
        }
        serializer =  InsumoSerializer(insumos,many=True,context=serializer_context)
        return Response({'count':insumos.count(),'next':None,'previous':None,'results':serializer.data})

    @action(detail=False)
    def get_insumo_by_quantity(self,request):
        user_email=request.GET['user_email']
        user = CustomUsers.objects.get(email=user_email)
        insumos = Insumo.objects.filter(user=user).order_by('cantidad')
        serializer_context = {
            'request': request,
        }
        serializer =  InsumoSerializer(insumos,many=True,context=serializer_context)
        return Response({'count':insumos.count(),'next':None,'previous':None,'results':serializer.data})

    @action(detail=False)
    def get_insumo_by_due_date(self,request):
        user_email=request.GET['user_email']
        user = CustomUsers.objects.get(email=user_email)
        insumos = Insumo.objects.filter(user=user).order_by('caducidad')
        serializer_context = {
            'request': request,
        }
        serializer =  InsumoSerializer(insumos,many=True,context=serializer_context)
        return Response({'count':insumos.count(),'next':None,'previous':None,'results':serializer.data})

    @action(detail=False)
    def get_insumo_by_category(self,request):
        user_email=request.GET['user_email']
        user = CustomUsers.objects.get(email=user_email)
        insumos = Insumo.objects.filter(user=user).order_by('categoria')
        serializer_context = {
            'request': request,
        }
        serializer =  InsumoSerializer(insumos,many=True,context=serializer_context)
        return Response({'count':insumos.count(),'next':None,'previous':None,'results':serializer.data})

    def post(self,request,pk):
        if(int(pk)>10000):
            insumo=Insumo.objects.get(pk=(int(pk)-10000))
            insumo.delete()
            return Response({"All": "OK"})
        if(int(pk)==0):
            insumo = Insumo()
        else:
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
        if(int(pk)==0):
            if request.FILES['image']!=None:
                file_image = request.FILES['image']
                insumo.image = file_image
            insumo.user = CustomUsers.objects.get(email=request_dict["user_email"])
        insumo.save()
        return Response({"All":"OK"})

    @action(detail=True,methods=['post'])
    def change_buy_date(self,request,pk=None):
        insumo = self.get_object()
        correct_date = datetime.datetime.strptime(request.data['new_date'],'%a %b %d %H:%M:%S CDT %Y').strftime('%Y-%m-%d %H:%M')
        insumo.fecha_ultima_compra=correct_date
        insumo.save()
        return Response({"All": "OK"})

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
    # parser_classes = (MultiPartParser,)
    serializer_class = LugarCompraSerializer
    #permission_classes = [permissions.IsAuthenticated]

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    @action(detail=False)
    def get_lugares_by_user(self,request):
        user_email=request.GET['user_email']
        lugares = LugarCompra.objects.filter(user=user_email)
        serializer_context = {
            'request': request,
        }
        serializer =  LugarCompraSerializer(lugares,many=True,context=serializer_context)
        return Response({'count':lugares.count(),'next':None,'previous':None,'results':serializer.data})

    def upload_docs(self):
        try:
            file = self.request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        insumo = Insumo.objects.create(img=file)