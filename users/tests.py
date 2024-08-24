from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import User


class UserTest(TestCase):
    """ Тестирование создания пользователей. """

    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        data = {
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        response = self.client.post(reverse('users:users-list'), data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, 'testuser@example.com')
