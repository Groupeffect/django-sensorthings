from __future__ import annotations

from django.test import SimpleTestCase
from django.test.utils import override_settings

from sensorthings import defaults as ST
from django.conf import settings


class ConfTests(SimpleTestCase):
    @override_settings(SENSORTHING_API_PREFIX=["xxx"])
    def test_override(self):
        assert settings.SENSORTHING_API_PREFIX == ["xxx"]
