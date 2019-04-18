import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

pytestmark = pytest.mark.django_db
TOKEN_URL = reverse('core:create_token')


class PublicApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_token_for_user(self):
        """"Test that a token is created for the user"""
        payload = {'email': 'test@scidev.co', 'password': 'testpass'}
        get_user_model().objects.create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials given"""
        user_info = {'email': 'test@scidev.co', 'password': 'testpass'}
        mixer.blend(get_user_model(), **user_info)
        payload = {'email': 'test@scidev.co', 'password': 'testpas'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user does not exists"""
        payload = {'email': 'test@scidev.co', 'password': 'testpas'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """test token is not created if email/password is missing"""
        res = self.client.post(TOKEN_URL, {'email': 'zzz', 'password': ''})

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
