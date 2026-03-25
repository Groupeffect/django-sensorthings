from django.conf import settings

if not hasattr(settings, "SENSORTHINGS_DISABLE_MODELS") or settings.SENSORTHINGS_DISABLE_MODELS is False:
    from sensorthings.db.models import *

else:
    print("set: SENSORTHINGS_DISABLE_MODELS = False, if you want to load models.")
