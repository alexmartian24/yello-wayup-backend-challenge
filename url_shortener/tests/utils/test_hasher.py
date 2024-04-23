"""Test cases for the hasher util."""

from django.test import TestCase
from shortener.utils.hasher import generate_hash


class HasherTestCase(TestCase):
    """
    Test case for URL model.

    Test cases:
      - generate_hash: Test the generate_hash method.
    """

    def test_generate_hash(self):
        """
        Test case for encode method.

        This method will test the encode method of URL model.

        "Y2RiNG" is base64 encoded value of the sha256 hash of the string "https://www.example.com"
        """
        url = "https://www.example.com"
        return_encoded_url = generate_hash(url)
        self.assertEqual("Y2RiNG", return_encoded_url)
