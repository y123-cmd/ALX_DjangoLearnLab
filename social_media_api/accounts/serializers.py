from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField(allow_blank=True, required=False)
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user, token

