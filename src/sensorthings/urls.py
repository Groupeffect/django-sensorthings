from django.urls import path, include

urlpatterns = [
    path("", include("sensorthings.routes.swagger")),
    path("jwt/", include("sensorthings.routes.jwt")),
    path("sensorthings/", include("sensorthings.routes.api")),
]