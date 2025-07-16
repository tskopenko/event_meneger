from rest_framework.routers import DefaultRouter
from event_model.views import EventViewSet, EventRegistrationViewSet
from django.urls import path, include
from user.views import UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"events", EventViewSet)
router.register(r"registrations", EventRegistrationViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

urlpatterns += [
    path("api/register/", UserRegistrationView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
