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
    *INSTALLED_APPS_OPTIONS["swagger"],
    *INSTALLED_APPS_OPTIONS["gis"],
]

SENSORTHING_API_PREFIX = "sensorthings"


# Build paths inside the project like this: BASE_DIR / 'subdir'.

DATABASE_OPTIONS = {
    "spatialite": {
        "ENGINE": "django.contrib.gis.db.backends.spatialite",
    },
    "postgis": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
    },
    "postgres": {
        "ENGINE": "django.db.backends.postgresql",
    },
}
