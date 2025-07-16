from rest_framework import serializers
from event_model.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "city", "location", "organizer"]
        read_only_fields = ["id", "organizer"]
