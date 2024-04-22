"""
URLMapping model.

Model for the URLMapping class.
"""

from django.db import models

class URLMapping(models.Model):
    """
    URLMapping model class.

    Attributes:
        original_url: URLField
        encoded_url: URLField
    """

    original_url = models.URLField(unique=True)
    encoded_url = models.URLField(unique=True)
