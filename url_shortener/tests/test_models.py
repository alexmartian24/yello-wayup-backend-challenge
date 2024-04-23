"""Unit tests for URLMapping Model."""

from django.test import TestCase
from shortener.models import URLMapping


class ModelTestCase(TestCase):
    """
    Test case for URL model.

    Tests:
        - Create URLMapping instance.
    """

    def test_create_URLMapping(self):
        """
        Test creating a URLMapping instance.

        Creates a URLMapping instance and checks if the original and encoded URL are correct.
        """
        URLMapping.objects.create(
            original_url="https://www.example.com",
            encoded_url="https://www.example-encoded.com",
        )

        url = URLMapping.objects.get(original_url="https://www.example.com")
        self.assertEqual(url.original_url, "https://www.example.com")
        self.assertEqual(url.encoded_url, "https://www.example-encoded.com")
