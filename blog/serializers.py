from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post

User = get_user_model()


class PostAuthorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):
    author = PostAuthorSerialzer()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author', )
