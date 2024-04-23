"""Unit tests for URL Validation util."""

from django.test import TestCase
from shortener.utils.url import validate_url, ValidationResult


class URLTestCase(TestCase):
    """
    Test case for URL model.

    Test cases:
      - test_validation_result_bool_success: Test ValidationResult __bool__ method.
      - test_validation_result_bool_failure: Test ValidationResult __bool__ method.
      - test_validation_result_str: Test ValidationResult __str__ method.
      - test_validation_result_int: Test ValidationResult __int__ method.
      - test_validation_result_get_message: Test ValidationResult get_message method.
      - test_validation_result_get_code: Test ValidationResult get_code method.
      - test_validate_url: Test validate_url method.
      - test_validate_url_invalid: Test validate_url method.
      - test_validate_url_empty: Test validate_url method.
      - test_validate_url_none: Test validate_url method.
    """

    def test_validation_result_bool_success(self):
        """
        Test case for ValidationResult __bool__ method.

        This method will test the __bool__ method of ValidationResult class.
        """
        result = ValidationResult(True, "URL is valid", 200)
        self.assertTrue(result)

    def test_validation_result_bool_failure(self):
        """
        Test case for ValidationResult __bool__ method.

        This method will test the __bool__ method of ValidationResult class.
        """
        result = ValidationResult(False, "Invalid URL", 400)
        self.assertFalse(result)

    def test_validation_result_str(self):
        """
        Test case for ValidationResult __str__ method.

        This method will test the __str__ method of ValidationResult class.
        """
        result = ValidationResult(False, "Invalid URL", 400)
        self.assertEqual(str(result), "Invalid URL")

    def test_validation_result_int(self):
        """
        Test case for ValidationResult __int__ method.

        This method will test the __int__ method of ValidationResult class.
        """
        result = ValidationResult(False, "Invalid URL", 400)
        self.assertEqual(int(result), 400)

    def test_validate_url(self):
        """
        Test case for validate_url method.

        This method will test the validate_url method of URL model.
        """
        url = "https://www.example.com"
        result = validate_url(url)
        self.assertTrue(result)
        self.assertEqual(result.message, "URL is valid")
        self.assertEqual(result.code, 200)

    def test_validate_url_invalid(self):
        """
        Test case for validate_url method.

        This method will test the validate_url method of URL model.
        """
        url = "www.example.com"
        result = validate_url(url)
        self.assertFalse(result)
        self.assertEqual(result.message, "Invalid URL")
        self.assertEqual(result.code, 400)

    def test_validate_url_empty(self):
        """
        Test case for validate_url method.

        This method will test the validate_url method of URL model.
        """
        url = ""
        result = validate_url(url)
        self.assertFalse(result)
        self.assertEqual(result.message, "URL parameter not found")
        self.assertEqual(result.code, 404)

    def test_validate_url_none(self):
        """
        Test case for validate_url method.

        This method will test the validate_url method of URL model.
        """
        url = None
        result = validate_url(url)
        self.assertFalse(result)
        self.assertEqual(result.message, "URL parameter not found")
        self.assertEqual(result.code, 404)
