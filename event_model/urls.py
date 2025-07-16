from rest_framework.routers import DefaultRouter
from event_model.views import EventViewSet, EventRegistrationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"events", EventViewSet)
router.register(r"registrations", EventRegistrationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
