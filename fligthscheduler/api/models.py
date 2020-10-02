from django.db import models
from django.utils.timezone import now

class Flight(models.Model):
    flight = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateTimeField(default=now, editable=False)
    destination = models.CharField(max_length=100, null=True, blank=True)
    scheduled_departure_time = models.CharField(max_length=10)
    assigned_plane_type = models.CharField(max_length=400)
    capacity = models.CharField(max_length=50, null=True, blank=True)
    seats_reserved = models.CharField(max_length=10, null=True, blank=True)
    seats_available = models.CharField(max_length=10, null=True, blank=True)

