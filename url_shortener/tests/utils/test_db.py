"""Unit tests for DB Util."""

from django.test import TestCase
from shortener.utils.db import create_url, get_url, URLMappingNotFound
from unittest.mock import patch


class DBTestCase(TestCase):
    """
    Test case for URL model.

    Test cases:
        - create_url_new_success: Create a new URLMapping instance.
        - create_url_existing_success: Create an existing URLMapping instance.
        - get_url_success: Get the original URL from the encoded URL.
        - get_url_failure: Try to get the original URL from a non-existing encoded URL.
    """

    def setUp(self):
        """
        Set up method.

        This method will be called before each test case.
        """
        self.BASE_URL_patcher = patch(
            "shortener.utils.db.BASE_URL", "http://testserver/"
        )
        self.BASE_URL_patcher.start()

        self.generate_hash_patcher = patch(
            "shortener.utils.db.generate_hash", return_value="1"
        )
        self.generate_hash_patcher.start()

    def test_create_url_new_success(self):
        """
        Test create_url method.

        Create a new URLMapping instance, and check if the encoded URL is returned.
        """
        original_url = "https://www.example.com"
        encoded_url = create_url(original_url)
        self.assertEqual(encoded_url, "http://testserver/1")

    def test_create_url_existing_success(self):
        """
        Test create_url method.

        Try to create an existing URLMapping instance, and check if the encoded URL is returned.
        """
        original_url = "https://www.example.com"
        encoded_url = create_url(original_url)
        self.assertEqual(encoded_url, "http://testserver/1")

        encoded_url = create_url(original_url)
        self.assertEqual(encoded_url, "http://testserver/1")

    def test_get_url_success(self):
        """
        Test get_url method.

        Get the original URL from the encoded URL.
        """
        original_url = "https://www.example.com"
        encoded_url = create_url(original_url)
        self.assertEqual(get_url(encoded_url), original_url)

    def test_get_url_failure(self):
        """
        Test get_url method with failure.

        Try to get the original URL from a non-existing encoded URL.
        """
        with self.assertRaises(URLMappingNotFound):
            get_url("http://testserver/2")
