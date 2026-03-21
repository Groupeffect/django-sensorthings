from __future__ import annotations

from django.apps import AppConfig
from django.core.checks import Tags, register

from sensorthings.checks import check_settings


class SensorthingsAppConfig(AppConfig):
    name = "sensorthings"
    verbose_name = "django-sensorthings"

    def ready(self) -> None:
        register(Tags.security)(check_settings)
