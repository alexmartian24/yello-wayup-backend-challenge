"""
This module contains the views.

The views in the module are:
    - encode_url: Encodes the original url
    - decode_url: Decodes the encoded url
"""
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .utils.db import create_url, get_url, URLMappingNotFound
from .utils.url import validate_url


@api_view(["GET"])
@permission_classes([AllowAny])
def root(request: Request) -> Response:
    """
    Root view.

    Returns a welcome message.

    Args:
        request: The request object.
    Returns:
        Response: The welcome message.
    """
    return Response("Welcome to the URL shortener API.")


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def encode_url(request: Request) -> Response:
    """
    Encode a url.

    Encodes the original url using the generate_hash function.
    Additionally, stores the original and encoded url in the URLMapping db.

    Args:
        request: The request object.
    Returns:
        Response: The encoded url.
    """
    data = request.data
    original_url = data.get("url")
    validationResult = validate_url(original_url)
    if not validationResult:
        return Response(
            {"error": str(validationResult)},
            status=int(validationResult),
        )
    encoded_url = create_url(original_url)
    return Response({"shortened_url": encoded_url})


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def decode_url(request: Request) -> Response:
    """
    Decode a url.

    Takes the encoded url and checks within the database for the original url.

    Args:
        request: The request object.
    Returns:
        Response: The original url.
    """
    data = request.data
    shortened_url = data.get("url")
    validationResult = validate_url(shortened_url)
    if not validationResult:
        return Response(
            {"error": str(validationResult)},
            status=int(validationResult),
        )
    try:
        original_url = get_url(shortened_url)
        return Response({"original_url": original_url})
    except URLMappingNotFound:
        return Response({"error": "Shortened URL not found"}, status=404)
