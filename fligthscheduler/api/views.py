from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import FlightSerializer, FlightMiniSerializer
from .models import Flight
from rest_framework.response import Response


def list(request, *args, **kwargs):
    flights = Flight.objects.all()
    serializer = FlightMiniSerializer(flights, many=True)
    return Response(serializer.data)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
