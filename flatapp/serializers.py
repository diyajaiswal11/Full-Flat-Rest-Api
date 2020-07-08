from rest_framework import serializers
from .models import RoomPreference, Rules, PropertyAmenities


class RoomPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoomPreference
        fields=('id','propertytype','moveindate','minimumbudget','maximumbudget','propertyamenities','rules')


class RulesSerializer(serializers.ModelSerializer):
    rules=RoomPreferenceSerializer(many=True)
    class Meta:
        model=Rules
        fields=('name','rules',)
        extra_kwargs = {'rules': {'required': False}}


class PropertyAmenitiesSerializer(serializers.ModelSerializer):
    propertyamenities=RoomPreferenceSerializer(many=True)
    class Meta:
        model=PropertyAmenities
        fields=('name','propertyamenities',)
        extra_kwargs = {'propertyamenities': {'required': False}}











