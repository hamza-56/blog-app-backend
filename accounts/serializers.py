from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
        )