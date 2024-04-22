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
from shortener.views import root, decode_url, encode_url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", root, name="root"),
    path("admin/", admin.site.urls),
    path("api/decode/", decode_url, name="decode"),
    path("api/encode/", encode_url, name="encode"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

