from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'flight', 'date', 'destination', 'scheduled_departure_time', 'assigned_plane_type', 'capacity', 'seats_reserved', 'seats_available']