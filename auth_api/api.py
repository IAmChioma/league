from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from rest_framework import status, views
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import AdminSerializer, UserSerializer, AllUserSerializer

UserModel = get_user_model()


class LoginView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password"))

        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username or password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response(AllUserSerializer(user).data)


class LogoutView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class CreateAdminView(CreateAPIView):
    model = get_user_model()
    serializer_class = AdminSerializer
    permission_classes = (AllowAny,)
