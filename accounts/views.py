from rest_framework.generics import CreateAPIView

from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer

User = get_user_model()


class RegisterView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
