=====================
django-sensorthings
=====================

A Django application for handling `OGC SensorThings API <https://www.ogc.org/standard/sensorthings/>`_ data. Provides
ready-to-use Django models, REST API views, serializers, and sensible default configurations for building SensorThings-
and TIGER geocoding-compatible services.

.. contents:: Table of Contents
   :depth: 2
   :local:


Requirements
============

- Python ≥ 3.12
- Django ≥ 6.0

Runtime dependencies (installed automatically):

- ``django-cors-headers`` ≥ 4
- ``django-extensions`` ≥ 4
- ``django-filter`` ≥ 25
- ``djangorestframework`` ≥ 3.16
- ``djangorestframework-gis`` ≥ 1.2
- ``djangorestframework-simplejwt`` ≥ 5.5
- ``drf-spectacular`` ≥ 0.28
- ``drf-spectacular-sidecar`` ≥ 2026.3

Runtime dependencies available for spatialite:

- ``libspatialite-dev`` (Debian/Ubuntu)
- ``spatialite-devel`` (Fedora/CentOS)
- ``libspatialite`` (macOS)
- ``libgdal-dev`` (Debian/Ubuntu)
- ``libgeos-dev`` (Debian/Ubuntu)
- ``libproj-dev`` (Debian/Ubuntu)
- ``libsqlite3-mod-spatialite`` (Debian/Ubuntu)
- ``libopenblas-dev`` (Debian/Ubuntu)

Installation
============

Install from PyPI:

.. code-block:: bash

   pip install django-sensorthings

Or via `uv <https://docs.astral.sh/uv/>`_:

.. code-block:: bash

   uv add django-sensorthings


Quick Start
===========

1. **Add the app and its dependencies to** ``INSTALLED_APPS``:

   You can use the pre-defined lists from ``sensorthings.defaults``, or add
   the entries by hand.

   .. code-block:: python


       # settings.py
      from sensorthings import defaults as ST

      INSTALLED_APPS = [
          *ST.INSTALLED_APPS_OPTIONS["core"],
          *ST.INSTALLED_APPS_OPTIONS["swagger"],
          *ST.INSTALLED_APPS_OPTIONS["gis"],
          "sensorthings",
          # ... your own apps
      ]
      
      # or if you want to use the default settings
      INSTALLED_APPS = ST.INSTALLED_APPS

2. **Include the URL configuration** in your project's root ``urls.py``:

   .. code-block:: python

      # urls.py
      from django.urls import path, include

      urlpatterns = [
          path("api/", include("sensorthings.routes.api")),
          path("api/", include("sensorthings.routes.jwt")),
          path("api/", include("sensorthings.routes.swagger")),
          # ...
      ]
    # or if you want to use the default settings
    from sensorthings import defaults as ST
    urlpatterns = [
        path("api/", include("sensorthings.urls")),
        # ...
    ]

   This will mount the following URL groups:

   ======================== ===========================================
   Prefix                   Description
   ======================== ===========================================
   ``/api/jwt/``            JWT authentication endpoints
   ``/api/sensorthings/``   SensorThings REST API (DRF router)
   ``/api/swagger/``        Swagger UI & OpenAPI schema
   ======================== ===========================================

3. **Apply migrations**:

   .. code-block:: bash

      python manage.py migrate

4. **Run the development server**:

   .. code-block:: bash

      python manage.py runserver

   Visit ``http://localhost:8000/api/swagger/`` to explore the auto-generated
   Swagger documentation.


Defaults
========

``sensorthings.defaults`` provides ready-made configuration dictionaries that
you can import into your project's ``settings.py``. Each setting can be
overridden as needed.

INSTALLED_APPS_OPTIONS
----------------------

A dictionary of app lists grouped by category:

.. code-block:: python

   from sensorthings.defaults import INSTALLED_APPS_OPTIONS

- ``INSTALLED_APPS_OPTIONS["core"]`` — Core Django apps, CORS, extensions,
  DRF, django-filter, and SimpleJWT.
- ``INSTALLED_APPS_OPTIONS["gis"]`` — ``django.contrib.gis`` and
  ``rest_framework_gis``.
- ``INSTALLED_APPS_OPTIONS["swagger"]`` — ``drf_spectacular`` and its sidecar.

DATABASE_OPTIONS
----------------

Pre-built ``DATABASES["default"]`` engine entries:

.. code-block:: python

   from sensorthings.defaults import DATABASE_OPTIONS

   DATABASES = {
       "default": {
           **DATABASE_OPTIONS["spatialite"],
           "NAME": "mydb",
           "USER": "myuser",
           "PASSWORD": "secret",
           "HOST": "localhost",
           "PORT": "5432",
       }
   }

Available keys:

=============== ==========================================
Key             Engine
=============== ==========================================
``spatialite``  ``django.contrib.gis.db.backends.spatialite``
``postgis``     ``django.contrib.gis.db.backends.postgis``
``postgres``    ``django.db.backends.postgresql``
=============== ==========================================

REST_FRAMEWORK
--------------

Default DRF settings including pagination, filtering, schema, and
authentication classes:

.. code-block:: python

   from sensorthings.defaults import REST_FRAMEWORK

Key settings:

- ``PAGE_SIZE``: ``1``
- ``DEFAULT_SCHEMA_CLASS``: ``drf_spectacular.openapi.AutoSchema``
- ``DEFAULT_PAGINATION_CLASS``: ``LimitOffsetPagination``
- ``DEFAULT_FILTER_BACKENDS``: ``DjangoFilterBackend``
- ``DEFAULT_AUTHENTICATION_CLASSES``: JWT, Basic, Token, and Session
  authentication.

SIMPLE_JWT
----------

SimpleJWT configuration:

.. code-block:: python

   from sensorthings.defaults import SIMPLE_JWT

Notable defaults:

- ``ACCESS_TOKEN_LIFETIME``: 24 hours
- ``REFRESH_TOKEN_LIFETIME``: 2 days
- ``AUTH_HEADER_TYPES``: ``("JWT",)``
- ``ALGORITHM``: ``HS256``

SPECTACULAR_SETTINGS
--------------------

drf-spectacular OpenAPI configuration:

.. code-block:: python

   from sensorthings.defaults import SPECTACULAR_SETTINGS

- ``OAS_VERSION``: ``3.0.3``
- ``TITLE``: Configurable via the ``SENSORTHINGS_SWAGGER_TITLE`` env variable
  (default: ``"Sensorthings"``).
- ``VERSION``: Configurable via the ``API_VERSION`` env variable (default:
  ``"1.0.2"``).
- Swagger UI served via the ``drf_spectacular_sidecar``.

SWAGGER_SETTINGS
----------------

.. code-block:: python

   from sensorthings.defaults import SWAGGER_SETTINGS

- ``LOGIN_URL``: ``"rest_framework:login"``
- ``LOGOUT_URL``: ``"rest_framework:logout"``

MIDDLEWARE
----------

A default middleware stack including CORS support:

.. code-block:: python

   from sensorthings.defaults import MIDDLEWARE

Includes ``SecurityMiddleware``, ``SessionMiddleware``,
``CorsMiddleware``, ``CommonMiddleware``, ``CsrfViewMiddleware``,
``AuthenticationMiddleware``, ``MessageMiddleware``, and
``XFrameOptionsMiddleware``.

SENSORTHINGS_ENABLE_PUBLIC_PRIVATE / SENSORTHINGS_ENABLE_OWNER
--------------------------------------------------------------

Boolean flags that control queryset visibility in ``MetaViewset``:

.. code-block:: python

   SENSORTHINGS_ENABLE_PUBLIC_PRIVATE = True  # default
   SENSORTHINGS_ENABLE_OWNER = True           # default

See the `Views`_ section for details on how these flags affect query
filtering.


Models
======

All models are defined in ``sensorthings.models`` and inherit from the
abstract ``MetaModel`` base class. Models are mapped to existing database
tables using ``db_table`` in the ``Meta`` class and are **unmanaged by
default** (no migrations will alter their schema).

SensorThings Core Models
------------------------

These models implement the `OGC SensorThings API
<https://www.ogc.org/standard/sensorthings/>`_ data model:

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Model
     - Table
     - Description
   * - ``Things``
     - ``things``
     - An object of the physical or virtual world.
   * - ``Locations``
     - ``locations``
     - The last known location of a Thing.
   * - ``HistLocations``
     - ``hist_locations``
     - Historical locations of a Thing.
   * - ``Sensors``
     - ``sensors``
     - Instruments that observe a property.
   * - ``ObservedProperties``
     - ``observed_properties``
     - The phenomenon being observed.
   * - ``Datastreams``
     - ``datastreams``
     - Groups observations from a sensor on a thing.
   * - ``Observations``
     - ``observations``
     - Individual measurement results.
   * - ``Features``
     - ``features``
     - Features of interest for observations.
   * - ``FeatureTypes``
     - ``feature_types``
     - Classification of features.
   * - ``Samplers``
     - ``samplers``
     - Devices or entities performing sampling.
   * - ``Samplings``
     - ``samplings``
     - Sampling events with location and time range.
   * - ``SamplingProcedures``
     - ``sampling_procedures``
     - Procedures used during sampling.
   * - ``PreparationProcedures``
     - ``preparation_procedures``
     - Procedures for preparing samples.
   * - ``PreparationSteps``
     - ``preparation_steps``
     - Individual steps in a preparation procedure.
   * - ``RelationRoles``
     - ``relation_roles``
     - Defines roles for entity relationships.

Association / Join Tables
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 30

   * - Model
     - Table
   * - ``ThingsLocations``
     - ``things_locations``
   * - ``LocationsHistLocations``
     - ``locations_hist_locations``
   * - ``DatastreamsObservedProperties``
     - ``datastreams_observed_properties``
   * - ``DatastreamsFeaturesUltimate``
     - ``datastreams_features_ultimate``
   * - ``FeaturesFeatureTypes``
     - ``features_feature_types``
   * - ``SamplerSamplingProcedure``
     - ``sampler_sampling_procedure``

Relation Models
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 30

   * - Model
     - Table
   * - ``RelatedDatastreams``
     - ``related_datastreams``
   * - ``RelatedFeatures``
     - ``related_features``
   * - ``RelatedObservations``
     - ``related_observations``
   * - ``RelatedThings``
     - ``related_things``

TIGER / Geocoding Models
------------------------

Provides models for US TIGER/Line geocoding tables:

``Addr``, ``Addrfeat``, ``Bg``, ``County``, ``CountyLookup``,
``CountysubLookup``, ``Cousub``, ``Edges``, ``Faces``, ``Featnames``,
``Place``, ``PlaceLookup``, ``State``, ``StateLookup``, ``Tabblock``,
``Tabblock20``, ``Tract``, ``Zcta5``, ``ZipLookup``, ``ZipLookupAll``,
``ZipLookupBase``, ``ZipState``, ``ZipStateLoc``, and various lookup tables
(``DirectionLookup``, ``SecondaryUnitLookup``, ``StreetTypeLookup``,
``LoaderLookuptables``, ``LoaderPlatform``, ``LoaderVariables``,
``GeocodeSettings``, ``GeocodeSettingsDefault``).

Utility Models
--------------

- ``Databasechangelog`` / ``Databasechangeloglock`` — Liquibase migration
  tracking tables.
- ``Layer`` / ``Topology`` — PostGIS topology support tables.
- ``PagcGaz``, ``PagcLex``, ``PagcRules`` — PAGC geocoder lexicon tables.


Routes
======

URL routing is defined in ``sensorthings.urls`` and split into three route
modules under ``sensorthings.routes``:

sensorthings.urls
-----------------

The main URL configuration that you include in your project:

.. code-block:: python

   from django.urls import path, include

   urlpatterns = [
       path("api/", include("sensorthings.urls")),
   ]

This mounts:

sensorthings.routes.swagger
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================ ============================================
URL                              View
================================ ============================================
``swagger/``                     ``SpectacularSwaggerView`` — interactive docs
``schema/``                      ``SpectacularJSONAPIView`` — OpenAPI schema
================================ ============================================

sensorthings.routes.jwt
~~~~~~~~~~~~~~~~~~~~~~~

================================ ============================================
URL                              View
================================ ============================================
``jwt/``                         ``TokenObtainPairView`` — obtain JWT pair
``jwt/verify/``                  ``TokenVerifyView`` — verify a token
``jwt/refresh/``                 ``TokenRefreshView`` — refresh a token
================================ ============================================

sensorthings.routes.api
~~~~~~~~~~~~~~~~~~~~~~~

All SensorThings and geocoding entity endpoints are registered with the DRF
``DefaultRouter`` and are mounted under the ``sensorthings/`` prefix. Each
model has a corresponding endpoint:

.. code-block:: text

   sensorthings/Things/
   sensorthings/Locations/
   sensorthings/Observations/
   sensorthings/Datastreams/
   sensorthings/Sensors/
   sensorthings/Features/
   sensorthings/ObservedProperties/
   ...

Each endpoint supports standard REST operations (list, create, retrieve,
update, partial update, destroy) depending on the viewset permissions.


Views
=====

All views are defined in ``sensorthings.views`` and inherit from the
``MetaViewset`` base class.

MetaViewset
-----------

.. code-block:: python

   from rest_framework import permissions
   from rest_framework.viewsets import ModelViewSet
   from rest_framework import filters
   from django_filters.rest_framework import DjangoFilterBackend

   class MetaViewset(ModelViewSet):
       serializer_class = None
       permission_classes = [permissions.IsAuthenticatedOrReadOnly]
       filter_backends = [
           DjangoFilterBackend,
           filters.SearchFilter,
           filters.OrderingFilter,
       ]

Key behaviour:

- **Permission**: ``IsAuthenticatedOrReadOnly`` — anonymous users get
  read-only access, authenticated users can write.
- **Filter backends**: ``DjangoFilterBackend`` (field-level filtering),
  ``SearchFilter`` (text search), and ``OrderingFilter`` (sort results).
- **Queryset**: Controlled by two Django settings:

  - ``SENSORTHINGS_ENABLE_PUBLIC_PRIVATE`` + ``SENSORTHINGS_ENABLE_OWNER``
    — returns objects owned by the current user **or** public, excluding
    private.
  - ``SENSORTHINGS_ENABLE_PUBLIC_PRIVATE`` only — returns public objects,
    excluding private.
  - ``SENSORTHINGS_ENABLE_OWNER`` only — returns objects owned by the
    current user.
  - Both ``False`` — returns all objects.

set_filterset_fields_exclude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A helper function that auto-generates ``filterset_fields`` and
``search_fields`` for a viewset by inspecting the model's fields and
excluding types that do not support text lookups:

.. code-block:: python

   from sensorthings.views import set_filterset_fields_exclude

   class MyViewset(MetaViewset):
       serializer_class = MySerializer
       filterset_fields = set_filterset_fields_exclude(serializer_class)
       search_fields = filterset_fields + ["id"]

Excluded field types: ``JSONField``, ``GeometryField``, ``PointField``,
``MultiPointField``, ``PolygonField``, ``MultiPolygonField``,
``LineStringField``, ``MultiLineStringField``, ``ForeignKey``,
``OneToOneField``, ``ManyToManyField``, ``ManyToManyRel``,
``ManyToOneRel``, ``GenericForeignKey``, ``FileField``, and
``CompositePrimaryKey``.

Entity Viewsets
---------------

Every model has a corresponding viewset that overrides ``serializer_class``.
Some viewsets also set ``filterset_fields`` and ``search_fields``
automatically:

.. code-block:: python

   class AddrViewset(MetaViewset):
       serializer_class = serializers.AddrSerializer
       filterset_fields = set_filterset_fields_exclude(serializer_class)
       search_fields = filterset_fields + ["id"]

   class ThingsViewset(MetaViewset):
       serializer_class = serializers.ThingsSerializer

   # ... one viewset per model

To customise the queryset or permissions, subclass the relevant viewset:

.. code-block:: python

   from sensorthings.views import ThingsViewset

   class MyThingsViewset(ThingsViewset):
       def get_queryset(self):
           return self.serializer_class.Meta.model.objects.filter(
               properties__project="demo"
           )


Serializers
===========

All serializers live in ``sensorthings.serializers`` and inherit from the
``MetaModelSerializer`` base class.

MetaModelSerializer
-------------------

.. code-block:: python

   from rest_framework import serializers

   class MetaModelSerializer(serializers.ModelSerializer):
       class Meta:
           model = None

Each entity serializer sets its ``Meta.model`` to the corresponding model and
exposes **all fields**:

.. code-block:: python

   class ThingsSerializer(MetaModelSerializer):
       class Meta:
           model = models.Things
           fields = "__all__"

   class SensorsSerializer(MetaModelSerializer):
       class Meta:
           model = models.Sensors
           fields = "__all__"

   # ... one serializer per model

To add computed fields or nested representations, subclass the serializer:

.. code-block:: python

   from sensorthings.serializers import DatastreamsSerializer

   class DetailedDatastreamsSerializer(DatastreamsSerializer):
       sensor_name = serializers.CharField(source="sensor.name", read_only=True)

       class Meta(DatastreamsSerializer.Meta):
           fields = "__all__"


Admin
=====

All models are automatically registered with the Django admin. Each admin
class dynamically lists all model fields in ``list_display``:

.. code-block:: python

   from django.contrib import admin
   from django.apps import apps

   app_models = apps.get_app_config("sensorthings").get_models()

   for model in app_models:
       class DynamicAdmin(admin.ModelAdmin):
           list_display = [field.name for field in model._meta.fields]

       admin.site.register(model, DynamicAdmin)

Access the admin at ``/admin/`` after creating a superuser:

.. code-block:: bash

   python manage.py createsuperuser


Full Example Project
====================

Below is a minimal ``settings.py`` for a new Django project using
``django-sensorthings``:

.. code-block:: python

    # settings.py
    from pathlib import Path
    from sensorthings import defaults as ST

    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = "django-insecure-ikb3ow6j856g7tue7a1#sy)*(onocx-#@kh)e7xv6hi8vv=7b1"

    DEBUG = True

    ALLOWED_HOSTS = ["*"]

    INSTALLED_APPS = ST.INSTALLED_APPS

    MIDDLEWARE = ST.MIDDLEWARE

    ROOT_URLCONF = "interface.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "interface.wsgi.application"

    DATABASES = {
        "default": {"NAME": BASE_DIR / "db.sqlite3", **ST.DATABASE_OPTIONS["spatialite"]}
    }

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]


    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_TZ = True

    STATIC_URL = "static/"

    REST_FRAMEWORK = ST.REST_FRAMEWORK

    SIMPLE_JWT = ST.SIMPLE_JWT

    SPECTACULAR_SETTINGS = ST.SPECTACULAR_SETTINGS

    SWAGGER_SETTINGS = ST.SWAGGER_SETTINGS


And the corresponding ``urls.py``:

.. code-block:: python

   # urls.py
   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path("admin/", admin.site.urls),
       path("api/", include("sensorthings.urls")),
   ]


Configuration
=============

Environment Variables
---------------------

==========================================  ====================================  ==========
Variable                                    Description                           Default
==========================================  ====================================  ==========
``SENSORTHINGS_SWAGGER_TITLE``              Title shown in the Swagger UI         ``Sensorthings``
``API_VERSION``                             API version in the OpenAPI schema     ``1.1``
==========================================  ====================================  ==========

Django Settings
---------------

Add these to your ``settings.py`` to control viewset queryset behaviour, models, and admin loading:

=============================================  =========================================  ==========
Setting                                        Description                                Default
=============================================  =========================================  ==========
``SENSORTHINGS_ENABLE_PUBLIC_PRIVATE``          Filter by ``is_public`` / ``is_private``    ``True``
``SENSORTHINGS_ENABLE_OWNER``                   Filter by ``has_owner`` (current user)      ``True``
``SENSORTHINGS_DISABLE_MODELS``                 Disable loading sensorthings models         ``False``
``SENSORTHINGS_DISABLE_ADMIN``                  Disable registering models in Django admin  ``False``
=============================================  =========================================  ==========

When both are ``True``, the queryset returns objects owned by the current
user **or** marked as public, while excluding private objects. Set either
to ``False`` to disable that filter dimension.


License
=======

Distributed under the **GPL-3.0** license. See ``LICENSE`` for details.


Links
=====

- Repository: https://github.com/groupeffect/django-sensorthings
- Changelog: https://github.com/groupeffect/django-sensorthings/blob/main/CHANGELOG.rst
