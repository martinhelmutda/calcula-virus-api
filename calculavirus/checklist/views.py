import datetime
from time import sleep

import pytz

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from calculavirus.checklist.serializers import ChecklistSerializer,ChecklistInsumoSerializer
from rest_framework.response import Response
from .models import *

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    #permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def get_buy_date(self,request,pk=None):
        checklist = self.get_object()
        insumos_checklist = ChecklistInsumo.objects.filter(checklist=checklist)
        num_insumos=0
        utc = pytz.UTC
        buy_date = utc.localize(datetime.datetime.now())
        max_priority = 0
        for insumo_row in insumos_checklist:
            num_insumos += 1
            if(insumo_row.insumo.prioridad>max_priority):
                max_priority = insumo_row.insumo.prioridad
                buy_date = insumo_row.insumo.fecha_ultima_compra + datetime.timedelta(days=insumo_row.insumo.duracion_promedio)
            elif(insumo_row.insumo.prioridad==max_priority):
                possible_buy_date = insumo_row.insumo.fecha_ultima_compra + datetime.timedelta(days=insumo_row.insumo.duracion_promedio)
                buy_date = max(buy_date,possible_buy_date)
        return Response({"buy_date":buy_date})

    @action(detail=False)
    def get_checklist_by_user(self,request):
        user_email=request.GET['user_email']
        checklists = Checklist.objects.filter(user__email=user_email)
        serializer_context = {
            'request': request,
        }
        serializer =  ChecklistSerializer(checklists,many=True,context=serializer_context)
        return Response({'count':checklists.count(),'next':None,'previous':None,'results':serializer.data})


class ChecklistInsumoViewSet(viewsets.ModelViewSet):
    queryset = ChecklistInsumo.objects.all()
    serializer_class = ChecklistInsumoSerializer
    #permission_classes = [permissions.IsAuthenticated]

    @action(detail=True,methods=['post','put'])
    def update_info(self,request,pk=None):
        checklist_insumo = self.get_object()
        if(request.data['comprado']=='false'):
            checklist_insumo.comprado = False
        else:
            checklist_insumo.comprado=True
        checklist_insumo.cantidad = request.data['cantidad']
        checklist_insumo.save()
        return Response({"All": "OK"})

    @action(detail=False,methods=['post'])
    def create_insumo_row(self,request):
        user=CustomUsers.objects.get(id=request.data['user_id'])
        num_checklists=Checklist.objects.filter(user=user).count()
        if(num_checklists==0):
            check1 = Checklist()
            check1.lugar_compra='Supermercado'
            check1.user = user
            check1.save()
            check2 = Checklist()
            check2.lugar_compra='Mercado'
            check2.user = user
            check2.save()
            check3 = Checklist()
            check3.lugar_compra='Tiendita'
            check3.user = user
            check3.save()
            check4 = Checklist()
            check4.lugar_compra='Otro'
            check4.user = user
            check4.save()
        sleep(4)
        checklist = Checklist.objects.get(user=user,lugar_compra=request.data['lugar_compra'])
        insumo = Insumo.objects.get(nombre=request.data['insumo_nombre'],user=user)
        checklist_row = ChecklistInsumo()
        checklist_row.insumo=insumo
        checklist_row.checklist=checklist
        checklist_row.user=user
        checklist_row.cantidad=0
        checklist_row.comprado=False
        checklist_row.save()
        return Response({"All": "OK"})