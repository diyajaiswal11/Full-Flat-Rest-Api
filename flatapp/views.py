from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from .serializers import RoomPreferenceSerializer, RulesSerializer, PropertyAmenitiesSerializer
from .models import RoomPreference, Rules, PropertyAmenities
from django.shortcuts import get_object_or_404
# Create your views here.


class PreferenceViewset(viewsets.ModelViewSet):
    queryset=RoomPreference.objects.all()
    serializer_class=RoomPreferenceSerializer


    def retrieve(self, request, pk=None):
        queryset = RoomPreference.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = RoomPreferenceSerializer(obj)
        print(obj)
        if obj.checked==None:
            msg={
                "data":serializer.data,
                "message":"Let admin verify",
            }
        elif obj.checked==True:
            msg={
                "data":serializer.data,
                "message":"Correct Data",
            }
        elif obj.checked==False:
            msg={
                "data":serializer.data,
                "message":"Incorrect Data",
            }
        return Response(msg)
