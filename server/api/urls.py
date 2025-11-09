from django.urls import path, include
from . import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('spots/', views.SpotListAPI.as_view(), name='spots-api'),
    path('challenges/', views.ChallengeListAPI.as_view(), name='challenges-api'),
]