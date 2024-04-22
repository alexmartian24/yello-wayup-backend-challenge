"""
This module does URL operations.

The methods in this module are:
    - validate_url: Validates the URL
"""

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class ValidationResult:
    """
    Validation result class.

    Attributes:
        is_valid (bool): The validation result.
        message (str): The validation message.
        code (int): The status code.
    """

    def __init__(self, is_valid: bool, message: str, code: int) -> None:
        """
        Initialize the validation result.

        Args:
            is_valid (bool): The validation result.
            message (str): The validation message.
            code (int): The status code.
        """
        self.is_valid = is_valid
        self.message = message
        self.code = code

    def __bool__(self) -> bool:
        """
        Return the validation result.

        Returns:
            bool: The validation result.
        """
        return self.is_valid

    def __str__(self) -> str:
        """
        Return the validation message.

        Returns:
            str: The validation message.
        """
        return self.message

    def __int__(self) -> int:
        """
        Return the status code.

        Returns:
            int: The status code.
        """
        return self.code


def validate_url(url: str) -> ValidationResult:
    """
    Validate the URL.

    Args:
        url (str): The URL to validate.

    Returns:
        ValidationResult: The validation result.
    """
    if not url:
        return ValidationResult(False, "URL parameter not found", 404)
    validate = URLValidator()
    try:
        validate(url)
    except ValidationError:
        return ValidationResult(False, "Invalid URL", 400)
    return ValidationResult(True, "URL is valid", 200)
