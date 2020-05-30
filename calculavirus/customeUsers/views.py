from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *

# Create your views here.
class CustomUsersViewSet(viewsets.ModelViewSet):
    queryset = CustomUsers.objects.all()
    serializer_class = CustomUsersSerializers
    permission_classes = [permissions.IsAuthenticated]
