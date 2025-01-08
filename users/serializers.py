from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели CustomUser.

    Attributes:
        Meta (class): Метакласс для настройки сериализатора.
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'telegram_chat_id')

class RegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации новых пользователей.

    Attributes:
        Meta (class): Метакласс для настройки сериализатора.
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """
        Создает нового пользователя с зашифрованным паролем.

        Args:
            validated_data (dict): Валидированные данные для создания
            пользователя.

        Returns:
            CustomUser: Созданный пользователь.
        """
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    """
    Сериализатор для аутентификации пользователей.

    Attributes:
        username (CharField): Поле для ввода имени пользователя.
        password (CharField): Поле для ввода пароля.
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        """
        Валидация данных для аутентификации пользователя.

        Args:
            data (dict): Данные для аутентификации.

        Returns:
            dict: Валидированные данные.

        Raises:
            ValidationError: Если аутентификация не удалась.
        """
        user = authenticate(username=data['username'],
                            password=data['password'])
        if user and user.is_active:
            return data
        raise serializers.ValidationError("Incorrect Credentials")
