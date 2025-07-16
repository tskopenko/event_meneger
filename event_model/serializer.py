from rest_framework import serializers
from event_model.models import Event, EventRegistration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "city", "location", "organizer"]
        read_only_fields = ["id", "organizer"]


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ["id", "event", "user", "registered_at"]
        read_only_fields = ["user", "registered_at"]
