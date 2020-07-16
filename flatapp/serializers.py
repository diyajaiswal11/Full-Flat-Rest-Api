from rest_framework import serializers
from .models import RoomPreference, Rules, PropertyAmenities, User, Payment


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('fname','lname',)
        

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'












