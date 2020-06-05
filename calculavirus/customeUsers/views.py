from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response

# Create your views here.
class CustomUsersViewSet(viewsets.ModelViewSet):
    queryset = CustomUsers.objects.all()
    serializer_class = CustomUsersSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_dict=request.data.dict()
        # print(request_dict)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
