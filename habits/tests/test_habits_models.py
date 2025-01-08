import pytest
from habits.models import Habit
from users.models import CustomUser

@pytest.mark.django_db
def test_create_habit():
    """
    Тест создания привычки.
    """
    user = CustomUser.objects.create_user(username='testuser',
                                          password='testpassword')
    habit = Habit.objects.create(
        user=user,
        place='Home',
        time='08:00:00',
        action='Drink water',
        is_pleasant=False,
        periodicity=1,
        execution_time=60,
        is_public=False
    )
    assert habit.action == 'Drink water'
    assert habit.user == user
