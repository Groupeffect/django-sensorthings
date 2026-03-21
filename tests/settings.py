from __future__ import annotations
from sensorthings import defaults as ST

ALLOWED_HOSTS = ["*"]

DATABASES = {"default": ST.DATABASE_OPTIONS["spatialite"]}

INSTALLED_APPS = [*ST.INSTALLED_APPS, "sensorthings"]

ROOT_URLCONF = "tests.urls"

TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates"}]

SECRET_KEY = "DEMOTESTSECRET"

SECURE_PROXY_SSL_HEADER = ("HTTP_FAKE_SECURE", "true")

USE_TZ = True

SENSORTHING_API_PREFIX = "api/sensor"
