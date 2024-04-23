"""
URLMapping model.

Model for the URLMapping class.
"""

from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class URLMapping(ExportModelOperationsMixin("url"), models.Model):
    """
    URLMapping model class.

    Attributes:
        original_url: URLField
        encoded_url: URLField
    """

    original_url = models.URLField(unique=True)
    encoded_url = models.URLField(unique=True)
