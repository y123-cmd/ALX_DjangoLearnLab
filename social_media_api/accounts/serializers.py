from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        # Use create_user to ensure hashed password
        user = get_user_model().objects.create_user(**validated_data)
        # Create and return a token for the user
        token = Token.objects.create(user=user)
        return user, token

