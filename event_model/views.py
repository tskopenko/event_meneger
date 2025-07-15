from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializer import EventSerializer


class EventModelViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
