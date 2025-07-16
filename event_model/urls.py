from rest_framework.routers import DefaultRouter
from event_model.views import EventViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"events", EventViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
