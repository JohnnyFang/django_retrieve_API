# -*- coding: utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "django_retrieve_API.settings")
import django
django.setup()

from django.contrib.auth import get_user_model
from review.models import Review


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


def main():
    # database = "C:\\sqlite\db\pythonsqlite.db"
    create_users_and_reviews()


def create_users_and_reviews():
    """ Creates 3 mock users"""
    get_user_model().objects.create_superuser(email="admin@user.com", password="Test12345")
    user_1 = get_user_model().objects.create_user(email="one@user.com", password="random123", name="user_1")
    user_2 = get_user_model().objects.create_user(email="two@user.com", password="pass123", name="user_2")

    sample_review(user_1, title="My review of AE", rating=3)
    sample_review(user_1, title="My review of Python for dummies", rating=5)
    sample_review(user_2, title="My review of TLJ", rating=2, summary="Pretty awful movie")
    sample_review(user_2, title="My review of TFA", rating=3, summary="an O.K. movie")


if __name__ == '__main__':
    main()
