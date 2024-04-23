# ShortLink

A simple URL shortener written with Django.

Refer to [design.md](design.md) for the full design.

## Build Instructions

``` sh
cp shortlink/env.sample shortlink/.env
docker build -t shortlink .
docker run -p 8000:8000 --env-file shortlink/.env shortlink
```

## Development

``` sh
cp shortlink/env.sample shortlink/.env
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
