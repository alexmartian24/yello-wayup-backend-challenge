"""
This file is used to register the models in the admin panel.

Models:
    - URLMapping: The model for storing the original and encoded URLs.
"""

from django.contrib import admin
from .models import URLMapping

admin.site.register(URLMapping)
