from rest_framework import serializers

from .models import Post
from users.serializers import RegistrationSerializer

class PostSerialzer(serializers.ModelSerializer):
    author = RegistrationSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'text', 'image', 'author'
        ]
