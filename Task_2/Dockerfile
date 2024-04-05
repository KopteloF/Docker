FROM python:3.9-alpine

RUN apk add --no-cache gcc musl-dev linux-headers

WORKDIR dj

COPY . .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONUNBUFFERED=1


CMD python manage.py runserver 0.0.0.0:8000