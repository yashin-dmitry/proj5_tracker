import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from users.models import CustomUser

@pytest.mark.django_db
def test_register_user():
    """
    Тест регистрации нового пользователя.
    """
    client = APIClient()
    url = reverse('register')
    data = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'newpassword'
    }

    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert CustomUser.objects.count() == 1
    assert CustomUser.objects.get().username == 'newuser'

@pytest.mark.django_db
def test_login_user():
    """
    Тест аутентификации пользователя.
    """
    client = APIClient()
    user = CustomUser.objects.create_user(username='testuser',
                                          password='testpassword')
    url = reverse('login')
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    response = client.post(url, data, format='json')
    assert response.status_code == 200
    assert response.data['username'] == 'testuser'
