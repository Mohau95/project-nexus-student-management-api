# Create your views here.
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from authapp.serializers import RegisterSerializer


class RegisterView:
    @classmethod
    def as_view(cls):
        pass


def post(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LoginView:
    @classmethod
    def as_view(cls):
        pass

    from rest_framework import generics

    class RegisterView(generics.CreateAPIView):
        serializer_class = RegisterSerializer

    class LoginView(generics.GenericAPIView):
        pass
