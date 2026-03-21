from __future__ import annotations

import re
from collections.abc import Sequence
from typing import Any
from urllib.parse import urlsplit

from django.conf import settings
from django.core.checks import CheckMessage, Error

from sensorthings.conf import conf


def is_sequence(thing: Any, type_or_types: type[Any] | tuple[type[Any], ...]) -> bool:
    return (
        isinstance(thing, Sequence)
        and not isinstance(thing, (str, bytes))
        and all(isinstance(x, type_or_types) for x in thing)
    )


def check_settings(**kwargs: Any) -> list[CheckMessage]:
    errors: list[CheckMessage] = []

    if not isinstance(conf.SENSORTHING_API_PREFIX, str):
        errors.append(
            Error(
                "SENSORTHING_API_PREFIX should be a string.",
                id="sensorthings.E001",
            )
        )

    return errors
