"""
This module contains the hasher function.

The hasher function in the module is:
    - generate_hash: Generates a hash value using the sha256 algorithm,
      then encodes it using url-safe base64.
"""

import base64
import hashlib


def generate_hash(url: str) -> str:
    """
    Generate a URL hash.

    Generates a hash value using the sha256 algorithm.
    The hash value is then encoded using base64.

    Args:
        url: The url to be hashed.
    Returns:
        The hashed url.
    """
    hash_url = hashlib.sha256(url.encode()).hexdigest()[:6]
    encoded_hash = base64.urlsafe_b64encode(hash_url.encode()).decode()[:6]
    return encoded_hash
