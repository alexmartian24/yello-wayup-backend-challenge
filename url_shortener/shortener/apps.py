"""
Django app configuration file.

This file is used to configure the app for Django.
"""

from django.apps import AppConfig


class ShortlinkServerConfig(AppConfig):
    """Configures the app for Django."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "shortener"
