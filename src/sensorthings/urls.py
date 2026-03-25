from django.urls import path, include
from django.conf import settings

urlpatterns = [
        path("", include("sensorthings.routes.swagger")),
        path("jwt/", include("sensorthings.routes.jwt")),
]

if not hasattr(settings, "SENSORTHINGS_DISABLE_MODELS") or settings.SENSORTHINGS_DISABLE_MODELS is False:
    urlpatterns += [
        path("sensorthings/", include("sensorthings.routes.api")),
    ]

