from django.conf import settings
if not settings.SENSORTHING_DISABLE_MODELS:
    from sensorthings.models import *