import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from habits.models import Habit
from users.models import CustomUser

@pytest.mark.django_db
def test_create_habit():
    """
    Тест создания привычки.
    """
    client = APIClient()
    user = CustomUser.objects.create_user(username='testuser', password='testpassword')
    client.force_authenticate(user=user)

    url = reverse('habit-list')
    data = {
        'place': 'Home',
        'time': '08:00:00',
        'action': 'Drink water',
        'is_pleasant': False,
        'periodicity': 1,
        'execution_time': 60,
        'is_public': False
    }

    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert Habit.objects.count() == 1
    assert Habit.objects.get().action == 'Drink water'


@pytest.mark.django_db
def test_list_habits():
    """
    Тест получения списка привычек текущего пользователя.
    """
    client = APIClient()
    user = CustomUser.objects.create_user(username='testuser',
                                          password='testpassword')
    client.force_authenticate(user=user)

    Habit.objects.create(user=user, place='Home', time='08:00:00',
                         action='Drink water', is_pleasant=False,
                         periodicity=1, execution_time=60, is_public=False)

    url = reverse('habit-list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['action'] == 'Drink water'
