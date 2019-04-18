from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime

from .custom_fields import IntegerRangeField
from django_retrieve_API.settings import AUTH_USER_MODEL


class Review(models.Model):
    title = models.CharField(max_length=64)
    rating = IntegerRangeField(min_value=0, max_value=5)
    summary = models.TextField(max_length=10000)
    ip_address = models.CharField(max_length=12)
    company = models.CharField(max_length=255)
    reviewer = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    submission_date = models.DateField(_("Date"), default=datetime.date.today)

    def __str__(self):
        return self.title

