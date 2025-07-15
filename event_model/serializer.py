from rest_framework import serializers
from event_model.models import Event


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False, max_length=255)
    date = serializers.DateField(format="%d-%m-%Y")
    city = serializers.CharField()
    location = serializers.CharField()
