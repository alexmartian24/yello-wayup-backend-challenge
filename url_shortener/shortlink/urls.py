"""
URL configuration for shortlink project.

Paths:
    - /: Root path
    - admin/: Django admin site
    - api/decode/: Decodes the encoded url
    - api/encode/: Encodes the original url    
"""
from django.contrib import admin
from django.urls import path
from shortener.views import decode_url, encode_url


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/decode/", decode_url, name="decode"),
    path("api/encode/", encode_url, name="encode"),
]
