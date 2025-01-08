from rest_framework import serializers
from .models import Habit
from .validators import validate_habit

class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit.

    Attributes:
        Meta (class): Метакласс для настройки сериализатора.
    """
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        """
        Валидация данных привычки.

        Args:
            data (dict): Данные привычки для валидации.

        Returns:
            dict: Валидированные данные.

        Raises:
            ValidationError: Если данные не проходят валидацию.
        """
        validate_habit(data)
        return data
