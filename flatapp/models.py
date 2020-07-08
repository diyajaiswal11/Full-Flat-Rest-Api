from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

# Create your models here.
property_choices= (
    ("Apartment","Apartment"),
    ("House","House"),
    ("Studio","Studio"),
)

class PropertyAmenities(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Rules(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name



class RoomPreference(models.Model):
    propertytype=models.CharField(max_length=20,choices=property_choices)
    moveindate=models.DateField(validators=[MinValueValidator(limit_value=date.today())])
    minimumbudget=models.IntegerField(default=0,validators=[MaxValueValidator(50000),MinValueValidator(0)])
    maximumbudget=models.IntegerField(default=0,validators=[MaxValueValidator(50000),MinValueValidator(0)])
    propertyamenities=models.ManyToManyField(PropertyAmenities,related_name='propertyamenities')
    rules=models.ManyToManyField(Rules,related_name='rules')

    def __str__(self):
        return self.propertytype

