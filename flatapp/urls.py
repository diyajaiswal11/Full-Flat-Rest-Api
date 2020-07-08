
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import PreferenceViewset


router = DefaultRouter()
router.register(r'preferences', PreferenceViewset, basename='preference')


urlpatterns = [
    path('', include(router.urls)),
]
