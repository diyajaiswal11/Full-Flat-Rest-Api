from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from .serializers import RoomPreferenceSerializer, RulesSerializer, PropertyAmenitiesSerializer
from .models import RoomPreference, Rules, PropertyAmenities
# Create your views here.


class PreferenceViewset(viewsets.ModelViewSet):
    queryset=RoomPreference.objects.all()
    serializer_class=RoomPreferenceSerializer

