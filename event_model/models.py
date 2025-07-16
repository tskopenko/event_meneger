from django.db import models
from user.models import User
from django.db.models.functions import Now
from location_field.models.plain import PlainLocationField


class Event(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField(db_default=Now())
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'])
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrowings")

    class Meta:
        verbose_name_plural = 'events'

    def __str__(self) -> str:
        return f'Event: {self.title} at {self.date} at {self.location}'


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_registrations")
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("event", "user")
