from django.urls import path
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularJSONAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    # TokenVerifyView
)

urlpatterns = [
    # path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
    path("jwt/", TokenObtainPairView.as_view(), name="jwt"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "schema/",
        SpectacularJSONAPIView().as_view(),
        name="schema",
    ),
]
