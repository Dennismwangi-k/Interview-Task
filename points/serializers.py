from rest_framework import serializers
from .models import ClosestPoints

class ClosestPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosestPoints
        fields = ['id', 'points_string', 'closest_pair', 'created_at']
