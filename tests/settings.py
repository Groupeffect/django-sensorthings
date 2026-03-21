from __future__ import annotations
from sensorthings.defaults import INSTALLED_APPS as ST_INSTALLED_APPS

ALLOWED_HOSTS = ["*"]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

INSTALLED_APPS = [*ST_INSTALLED_APPS, "sensorthings"]

ROOT_URLCONF = "tests.urls"

TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates"}]

SECRET_KEY = "DEMOTESTSECRET"

SECURE_PROXY_SSL_HEADER = ("HTTP_FAKE_SECURE", "true")

USE_TZ = True

SENSORTHING_API_PREFIX = "api/sensor"
