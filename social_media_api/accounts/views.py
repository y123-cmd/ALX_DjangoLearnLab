from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

# Custom User Model
User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        
        if user is None:
            return Response({"detail": "Invalid credentials"}, status=400)
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserRegistrationSerializer

    def get_object(self):
        return self.request.user

