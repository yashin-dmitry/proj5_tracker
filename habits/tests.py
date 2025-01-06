from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Habit

class HabitTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        response = self.client.post('/api/habits/', {
            'place': 'Home',
            'time': '08:00:00',
            'action': 'Drink water',
            'is_pleasant': False,
            'periodicity': 1,
            'execution_time': 60,
            'is_public': False
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.get().action, 'Drink water')
