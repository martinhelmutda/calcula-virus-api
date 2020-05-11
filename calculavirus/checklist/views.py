from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from calculavirus.checklist.serializers import ChecklistSerializer,ChecklistInsumoSerializer
from .models import *

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ChecklistInsumoViewSet(viewsets.ModelViewSet):
    queryset = ChecklistInsumo.objects.all()
    serializer_class = ChecklistInsumoSerializer
    #permission_classes = [permissions.IsAuthenticated]