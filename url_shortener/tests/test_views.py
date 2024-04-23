"""Unit tests for URL Shortener Views."""

from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from shortener.utils.db import create_url
from unittest.mock import patch


class URLShortenerViewsTestCase(APITestCase):
    """
    Test case for URL Shortener Views.

    Test cases:
        - test_root: Test root view.
        - test_decode_url: Test decode_url view.
        - test_encode_url: Test encode_url view.
    """

    def setUp(self):
        """
        Set up method.

        This method will be called before each test case.
        """
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def test_root(self):
        """
        Test root view.

        This method will test the root view.
        """
        url = reverse("root")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_encode_url(self):
        """
        Test encode_url view.

        This method will test the encode_url view.
        """
        with patch("shortener.utils.db.create_url") as mock_create_url:
            mock_create_url.return_value = "http://testserver/1"

            url = reverse("encode")
            data = {"url": "https://www.example.com"}
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 200)

    def test_decode_url(self):
        """
        Test decode_url view.

        This method will test the decode_url view.
        """
        encoded_url = create_url("https://www.example.com")
        data = {"url": encoded_url}
        url = reverse("decode")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
