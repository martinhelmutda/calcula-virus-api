from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from calculavirus.checklist.serializers import ChecklistSerializer,ChecklistInsumoSerializer
from .models import *

class ChecklistViewSet(viewsets.ModelViewSets):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    permission_classes = [permissions.isAuthenticated]

class ChecklistInsumoViewSet(viewsets.ModelViewSets):
    queryset = ChecklistInsumo.objects.all()
    serializer_class = ChecklistInsumoSerializer
    permission_classes = [permissions.isAuthenticated]