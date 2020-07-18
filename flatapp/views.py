from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RoomPreferenceSerializer, RulesSerializer, PropertyAmenitiesSerializer, UserSerializer, PaymentSerializer
from .models import RoomPreference, Rules, PropertyAmenities, User, Payment
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from datetime import date, datetime
from django.utils import timezone
# Create your views here.


class ChatAPIView(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk,format=None):
        
        user = self.get_object(pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
        

class PreferenceAPIView(APIView):

    def get_object(self, pk):
        try:
            return RoomPreference.objects.get(pk=pk)
        except RoomPreference.DoesNotExist:
            raise Http404


    def get(self, request, pk,format=None):
        #queryset = RoomPreference.objects.all()
        obj = self.get_object(pk)
        serializer = RoomPreferenceSerializer(obj)
        
        if obj.checked==None:
            msg={
                "data":serializer.data,
                "message":"Wait for the admin to verify your details.",
            }
        elif obj.checked==True:
            msg={
                "data":serializer.data,
                "message":"Your details have been successfully verified by the Admin.",
            }
        elif obj.checked==False:
            msg={
                "data":serializer.data,
                "message":"Your details seem to be incorrect/inappropriate as verified by admin.",
            }
        return Response(msg)


class PaymentMixin(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class Trying(APIView):
    def get(self,request,format=None):

        fname = self.request.GET.get('fname', False)
        lname = self.request.GET.get('lname', False)
        plan_id = self.request.GET.get('plan_id', False)

        payment=Payment.objects.get(plan_id=int(plan_id))
        serializer = PaymentSerializer(payment)
        payment=Payment.objects.get(user_id=serializer.data['user_id'])
        print(obj)
        user=User.objects.create(fname=fname,lname=lname,plan_id=obj)

        return HttpResponse('Hi')


class PaymentDataUpdate(APIView):

    def get(self,request,format=None):
        payment_id = self.request.GET.get('payment_id', False)
        user_id = self.request.GET.get('user_id', False)
        plan_id = self.request.GET.get('plan_id', False)
        paid_amount=self.request.GET.get('paid_amount', False)
        plan_validity=self.request.GET.get('plan_validity', False)


        payment=Payment.objects.create(payment_id=payment_id,user_id=int(user_id),plan_id=int(plan_id))
    
        user=User.objects.filter(pk=int(user_id)).update(paid=True,plan_id=int(plan_id),payment_status="Plan Activated",paid_amount=int(paid_amount),plan_validity=int(plan_validity))
        serializer = PaymentSerializer(payment)
        print(serializer.data['user_id'])
        return Response(serializer.data)
        
class PaymentTable(APIView):

    def get(self,request,format=None):
        payment=Payment.objects.get(payment_id=1104)
        serializer=PaymentSerializer(payment)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None, *args, **kwargs):
        payment = Payment.objects.create(
            payment_id= request.data.get('payment_id'),
            user_id=request.data.get('user_id'),
            plan_id=request.data.get('plan_id'),
            plan_validity=request.data.get('plan_validity'),
            paid_amount=request.data.get('paid_amount')
            
        )

        payment.expiration_date = date.today() + datetime.timedelta(days=request.data.get('plan_validity'))
        payment.payment_status="Plan Activated"
        payment_status.paid=True


        return HttpResponse({"Payment saved":"True"})
        


        

    
   