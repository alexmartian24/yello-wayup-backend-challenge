FROM --platform=$BUILDPLATFORM python:3.11-alpine AS builder

EXPOSE 8000
WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
