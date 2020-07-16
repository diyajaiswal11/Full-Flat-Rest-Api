
from django.urls import path, include
from . import views
from django.conf.urls import url

from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import PreferenceAPIView, ChatAPIView, PaymentMixin, PaymentDataUpdate


#router = DefaultRouter()
#router.register(r'preferences', PreferenceViewset, basename='preference')


urlpatterns = [
    path('property/<int:pk>/', PreferenceAPIView.as_view()),
    path('chat/<int:pk>/', ChatAPIView.as_view()),
    url(r'^payment/$',PaymentMixin.as_view()),
    url(r'^paymentdata/$', PaymentDataUpdate.as_view()),
    #path('', include(router.urls)),
]
