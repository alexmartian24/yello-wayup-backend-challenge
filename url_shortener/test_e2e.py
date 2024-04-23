"""
This script demonstrates how to send a POST request to a protected view in Django REST framework.

The script performs the following steps:
1. Obtains a JWT token by sending a POST request to the token endpoint.
2. Sends a POST request to a protected view with the JWT token in the Authorization header.
3. Prints the response from the protected view.
"""

import requests
import sys

username = "admin"
password = "admin"
url = "https://example.com"
if len(sys.argv) == 4:
    username = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
if len(sys.argv) == 2:
    url = sys.argv[1]

base_url = "http://localhost:8000"

credentials = {
    "username": username,
    "password": password,
}

token_url = f"{base_url}/api/token/"
response = requests.post(token_url, data=credentials)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data["access"]
    print("Token obtained successfully.")
else:
    print("Failed to obtain token.")
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")
    exit(1)

endpoint_url = f"{base_url}/api/encode/"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

request_body = {
    "url": url,
}

response = requests.post(endpoint_url, headers=headers, json=request_body)

if response.status_code == 200:
    print("Request successful.")
    print(f"Response: {response.text}")
else:
    print("Request failed.")
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")


endpoint_url = f"{base_url}/api/decode/"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

request_body = {
    "url": response.json()["shortened_url"],
}

response = requests.post(endpoint_url, headers=headers, json=request_body)

if response.status_code == 200:
    print("Request successful.")
    print(f"Response: {response.text}")
else:
    print("Request failed.")
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")
