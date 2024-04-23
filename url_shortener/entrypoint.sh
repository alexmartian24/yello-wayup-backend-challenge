#!/bin/sh

python3 manage.py createsuperuser --username admin --email admin@admin.com --no-input

exec "$@"
