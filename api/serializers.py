from rest_framework import serializers
from challenges.models import Spot, Challenge, Visual


class VisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visual
        fields = ['id', 'file', 'file_type', 'processed_url']


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ['id', 'name', 'longitude', 'latitude', 'description', 'date', 'approved', 'event']


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'points', 'user', 'longitude', 'latitude', 'description', 'date', 'approved', 'event']
