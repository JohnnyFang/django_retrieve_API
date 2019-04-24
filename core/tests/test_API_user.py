import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

pytestmark = pytest.mark.django_db
CREATE_USER_URL = reverse('core:create_user')


class UserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        """Test user creation"""
        payload = {'email': 'test@scidev.co', 'password': 'test54321', 'name': 'user1'}

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating user that already exists fails"""
        payload = {'email': 'test@scidev.co', 'password': 'test54321', 'name': 'user1'}
        get_user_model().objects.create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
