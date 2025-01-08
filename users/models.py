from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя.

    Attributes:
        telegram_chat_id (str): Идентификатор чата Telegram.
    """
    telegram_chat_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        """
        Возвращает строковое представление пользователя.

        Returns:
            str: Строковое представление пользователя.
        """
        return self.username
