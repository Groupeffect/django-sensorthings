from __future__ import annotations

from django.conf import settings


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
