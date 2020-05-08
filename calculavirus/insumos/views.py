from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from calculavirus.insumos.serializers import UserSerializer, GroupSerializer, InsumoSerializer
from .models import *

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
    permission_classes = [permissions.IsAuthenticated]