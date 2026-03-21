from __future__ import annotations

from collections.abc import Sequence
from re import Pattern
from typing import cast

from django.conf import settings

from sensorthings.defaults import default_headers, default_methods


class Settings:
    """
    Shadow Django's settings with a little logic
    """

    @property
    def SENSORTHING_API_PREFIX(self) -> str:
        return getattr(settings, "SENSORTHING_API_PREFIX", "sensorthings")
    @property
    def SENSORTHING_DISABLE_MODELS(self) -> bool:
        return getattr(settings, "SENSORTHING_DISABLE_MODELS", False)

conf = Settings()
