from rest_framework import serializers
from .models import Itinerary, ItineraryOption

class ItineraryOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryOption
        fields = ['id', 'description', 'location', 'created_at']

class ItinerarySerializer(serializers.ModelSerializer):
    options = ItineraryOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = ['id', 'user', 'title', 'start_date', 'end_date', 'created_at', 'updated_at', 'options']
        read_only_fields = ['user']  # usually user is set by the view, not the client
