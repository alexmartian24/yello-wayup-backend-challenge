"""
This module contains the db interaction.

The methods in this module are:
    - create_url: creates/gets a URLMapping instance
    - get_url: gets a URLMapping instance
"""

from ..models import URLMapping
from .hasher import generate_hash
from django.conf import settings


BASE_URL = "https://short.est"


class URLMappingNotFound(Exception):
    """
    Exception raised when a URLMapping instance is not found.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize the URLMappingNotFound exception.

        Args:
            message (str): The error message.
        """
        self.message = message
        super().__init__(self.message)


def create_url(original_url: str) -> str:
    """
    Create a URLMapping instance with the original URL.

    If a URLMapping instance with the original URL already exists, it returns the encoded URL.

    Additionally, collision likelihood is low. Further work could be done to check if
    there is a collision before creating the new URLMapping instance.

    Args:
        original_url (str): The original URL.

    Returns:
        str: The encoded URL.
    """
    encoded_url = BASE_URL + generate_hash(original_url)
    url_mapping, created = URLMapping.objects.get_or_create(
        original_url=original_url, encoded_url=encoded_url
    )
    return url_mapping.encoded_url


def get_url(encoded_url: str) -> str:
    """
    Get the original URL from the encoded URL.

    Args:
        encoded_url (str): The encoded URL.

    Returns:
        str: The original URL.
    """
    try:
        url_mapping = URLMapping.objects.get(encoded_url=encoded_url)
        return url_mapping.original_url
    except URLMapping.DoesNotExist:
        raise URLMappingNotFound("URLMapping instance not found.")
