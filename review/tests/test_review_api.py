import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from review.models import Review
from review.serializers import ReviewSerializer

pytestmark = pytest.mark.django_db

REVIEWS_URL = reverse('review:review-list')


def sample_review(reviewer, **params):
    """creates and returns a sample review"""
    defaults = {
        'title': 'sample review!',
        'rating': 4,
        'ip_address': "197.0.0.1",
        'company': "company for sample review",
        'summary': "sample summary for testing!",
    }
    defaults.update(params)

    return Review.objects.create(reviewer=reviewer, **defaults)


class PublicReviewApiTests(TestCase):
    """Test unauthenticated review API access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required!!"""
        res = self.client.get(REVIEWS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateReviewApiTest(TestCase):
    """Test authenticated review API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@test.co', 'testpassword'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_reviews(self):
        """test retrieving a list of reviews"""
        sample_review(reviewer=self.user)
        sample_review(reviewer=self.user)

        res = self.client.get(REVIEWS_URL)

        reviews = Review.objects.filter(reviewer=self.user).order_by('-id')
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_reviews_limited_to_user(self):
        """test users cannot see reviews submitted by other users """
        user2 = get_user_model().objects.create_user(
            'otheruser@test.co', 'testpass'
        )
        sample_review(reviewer=user2)
        sample_review(reviewer=self.user)

        res = self.client.get(REVIEWS_URL)

        reviews = Review.objects.filter(reviewer=self.user).order_by('-id')
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(len(res.data), 1)

    def test_create_review(self):
        """Test review creation"""
        payload = {
            'title': 'my test review',
            'rating': 4,
            'company': "some weird company",
            'reviewer': self.user.id,
            'summary': 'some random summary just for testing',
        }
        res = self.client.post(REVIEWS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        review = Review.objects.get(id=res.data['id'])
        for key in payload.keys():
            if key == 'reviewer':
                self.assertEqual(payload[key], self.user.id)
            else:
                self.assertEqual(payload[key], getattr(review, key))
