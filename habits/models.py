from django.db import models
from django.conf import settings

class Habit(models.Model):
    """
    Модель привычки.

    Attributes:
        user (CustomUser): Пользователь, создавший привычку.
        place (str): Место, в котором необходимо выполнять привычку.
        time (TimeField): Время, когда необходимо выполнять привычку.
        action (str): Действие, которое представляет собой привычку.
        is_pleasant (bool): Признак приятной привычки.
        related_habit (Habit): Связанная привычка.
        periodicity (int): Периодичность выполнения привычки.
        reward (str): Вознаграждение за выполнение привычки.
        execution_time (int): Время, которое предположительно потратит
        пользователь на выполнение привычки.
        is_public (bool): Признак публичности привычки.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    is_pleasant = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', null=True, blank=True,
                                      on_delete=models.SET_NULL)
    periodicity = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=255, null=True, blank=True)
    execution_time = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        """
        Возвращает строковое представление привычки.

        Returns:
            str: Строковое представление привычки.
        """
        return self.action
