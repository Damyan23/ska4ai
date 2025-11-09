from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.db import models
from challenges.models import Spot, Challenge, Visual
from .serializers import SpotSerializer, ChallengeSerializer, VisualSerializer

# Create your views here.
class SpotListAPI(generics.ListCreateAPIView):
    serializer_class = SpotSerializer
    
    def get_queryset(self):
        # Prefetch related visuals to avoid N+1 queries
        return Spot.objects.filter(approved=True).prefetch_related('visual_set').order_by('-date')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        # Add visuals to each spot
        spots_data = serializer.data
        for i, spot in enumerate(queryset):
            visuals = Visual.objects.filter(spot=spot)
            visual_serializer = VisualSerializer(visuals, many=True)
            spots_data[i]['visuals'] = visual_serializer.data
        
        return Response({
            'count': len(spots_data),
            'results': spots_data
        })


class ChallengeListAPI(generics.ListCreateAPIView):
    serializer_class = ChallengeSerializer
    
    def get_queryset(self):
        return Challenge.objects.filter(approved=True).order_by('-date')