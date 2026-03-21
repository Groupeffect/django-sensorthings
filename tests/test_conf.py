from __future__ import annotations

from django.test import SimpleTestCase
from django.test.utils import override_settings

from sensorthings.conf import conf


class ConfTests(SimpleTestCase):
    @override_settings(SENSORTHING_API_PREFIX=["xxx"])
    def test_override(self):
        assert conf.SENSORTHING_API_PREFIX == ["xxx"]
