import pytest
import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


def create_review():
    reviewer = mixer.blend(get_user_model(), id=99)
    review = mixer.blend(
        "review.Review",
        rating=5,
        title="Fireball",
        ip_address="197.0.0.1",
        company="some weird company",
        reviewer=reviewer,
        summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore"
                " et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
                "aliquip ex ea commodo consequat. "
    )
    return review


class TestReview(TestCase):
    def test_user_model(self):
        obj = mixer.blend("review.Review")
        assert obj.pk == 1, 'Should create a review instance'

    def test_review_str(self):
        review = create_review()

        self.assertEqual(str(review), review.title)
