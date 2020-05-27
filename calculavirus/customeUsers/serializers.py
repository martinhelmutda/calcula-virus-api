from .models import *
from rest_framework import serializers

class CustomUsersSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUsers
        fields = ['id', 'name', 'email']
