from rest_framework import generics
from user.serializers import UserRegistrationSerializer
from user.models import User


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
