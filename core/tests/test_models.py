import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestModel(TestCase):
    def test_user_model(self):
        obj = mixer.blend(get_user_model())
        assert obj.pk == 1, 'Should create a User instance'

    def test_create_user(self):
        """Test creating a new user"""
        user = get_user_model().objects.create_user(
            'user@test.com',
            'test54321'
        )
        self.assertTrue(user.is_active)
        self.assertTrue(user.email, 'user@test.com')

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
