from rest_framework import serializers
from app.models import Car
from rest_framework import generics

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields ='__all__'

