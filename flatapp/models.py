from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from django.utils import timezone

# Create your models here.
property_choices= (
    ("Apartment","Apartment"),
    ("House","House"),
    ("Studio","Studio"),
)

nullboolean = (
    (None, "Null"),
    (True, "True"),
    (False, "False")
)

payment_status_choices = (
    ("No Plan Chosen","No Plan Chosen"),
    ("Plan Activated","Plan Activated"),
    ("Plan Expired","Plan Expired"),
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
    checked=models.NullBooleanField(choices=nullboolean,default=None)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return self.propertytype




class User(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    paid=models.BooleanField(default=False)
    plan_id=models.IntegerField(default=0)
    payment_status=models.CharField(choices=payment_status_choices,default="No Plan Chosen",max_length=30)
    paid_date=models.DateField(default=date.today)
    paid_amount=models.IntegerField(default=0)
    plan_validity=models.IntegerField(default=0)
       

    def __str__(self):
        return self.fname



class Payment(models.Model):
    payment_id=models.CharField(max_length=50)
    user_id=models.IntegerField(default=0)
    plan_id=models.IntegerField(default=0)
    payment_date=models.DateField(default=date.today)

    



