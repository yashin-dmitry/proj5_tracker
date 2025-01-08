import pytest
from users.models import CustomUser

@pytest.mark.django_db
def test_create_user():
    """
    Тест создания пользователя.
    """
    user = CustomUser.objects.create_user(username='testuser',
                                          password='testpassword')
    assert user.username == 'testuser'
    assert user.check_password('testpassword')

@pytest.mark.django_db
def test_create_superuser():
    """
    Тест создания суперпользователя.
    """
    admin_user = CustomUser.objects.create_superuser(username='admin',
                                                     password='adminpassword')
    assert admin_user.is_superuser
    assert admin_user.is_staff
