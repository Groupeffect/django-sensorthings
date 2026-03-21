INSTALLED_APPS_OPTIONS = {
    "core": [
        "corsheaders",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django_extensions",
        "django_filters",
        "rest_framework",
        "rest_framework_simplejwt",
    ],
    "gis": [
        "django.contrib.gis",
        "rest_framework_gis",
    ],
    "swagger": [
        "drf_spectacular",
        "drf_spectacular_sidecar",
    ],
}

INSTALLED_APPS = [
    *INSTALLED_APPS_OPTIONS["core"],
    *INSTALLED_APPS_OPTIONS["gis"],
    *INSTALLED_APPS_OPTIONS["swagger"],
]

SENSORTHING_API_PREFIX = "sensorthings"
