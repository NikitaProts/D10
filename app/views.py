from django.shortcuts import render
from app.models import Car
from django.views.generic.list import ListView
from app.serializers import CarSerializer
from rest_framework import generics,serializers 
from django_filters.rest_framework import DjangoFilterBackend

class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends  = [DjangoFilterBackend]
    filterset_fields  = '__all__'

