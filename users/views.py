from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, authenticate
from .models import CustomUser
from .serializers import (CustomUserSerializer, RegisterSerializer,
                          LoginSerializer)

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели CustomUser.

    Attributes:
        queryset (QuerySet): Набор объектов модели CustomUser.
        serializer_class (CustomUserSerializer): Класс сериализатора
        для модели CustomUser.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class RegisterView(generics.CreateAPIView):
    """
    Представление для регистрации новых пользователей.

    Attributes:
        queryset (QuerySet): Набор объектов модели CustomUser.
        permission_classes (list): Список классов разрешений.
        serializer_class (RegisterSerializer): Класс сериализатора
        для регистрации пользователей.
    """
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        """
        Создает нового пользователя.

        Args:
            request (Request): Объект запроса.

        Returns:
            Response: Ответ с данными созданного пользователя.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

class LoginView(generics.GenericAPIView):
    """
    Представление для аутентификации пользователей.

    Attributes:
        serializer_class (LoginSerializer): Класс сериализатора для
        аутентификации пользователей.
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        Аутентифицирует пользователя и возвращает данные пользователя.

        Args:
            request (Request): Объект запроса.

        Returns:
            Response: Ответ с данными аутентифицированного пользователя.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])
        if user:
            login(request, user)
            return Response(CustomUserSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
