from __future__ import annotations

from django.test import SimpleTestCase, override_settings
from django.urls import reverse, resolve
from rest_framework import permissions
from rest_framework.test import APIClient

from sensorthings import views, serializers, models
from sensorthings.views import set_filterset_fields_exclude, MetaViewset


# ---------------------------------------------------------------------------
# Helper: all (basename, ViewsetClass) pairs from the router
# ---------------------------------------------------------------------------
VIEWSET_REGISTRY = [
    ("addr", views.AddrViewset),
    ("addrfeat", views.AddrfeatViewset),
    ("bg", views.BgViewset),
    ("county", views.CountyViewset),
    ("countylookup", views.CountyLookupViewset),
    ("countysublookup", views.CountysubLookupViewset),
    ("cousub", views.CousubViewset),
    ("databasechangelog", views.DatabasechangelogViewset),
    ("databasechangeloglock", views.DatabasechangeloglockViewset),
    ("datastreams", views.DatastreamsViewset),
    ("datastreamsfeaturesultimate", views.DatastreamsFeaturesUltimateViewset),
    ("datastreamsobservedproperties", views.DatastreamsObservedPropertiesViewset),
    ("directionlookup", views.DirectionLookupViewset),
    ("edges", views.EdgesViewset),
    ("faces", views.FacesViewset),
    ("featnames", views.FeatnamesViewset),
    ("featuretypes", views.FeatureTypesViewset),
    ("features", views.FeaturesViewset),
    ("featuresfeaturetypes", views.FeaturesFeatureTypesViewset),
    ("geocodesettings", views.GeocodeSettingsViewset),
    ("geocodesettingsdefault", views.GeocodeSettingsDefaultViewset),
    ("histlocations", views.HistLocationsViewset),
    ("layer", views.LayerViewset),
    ("loaderlookuptables", views.LoaderLookuptablesViewset),
    ("loaderplatform", views.LoaderPlatformViewset),
    ("loadervariables", views.LoaderVariablesViewset),
    ("locations", views.LocationsViewset),
    ("locationshistlocations", views.LocationsHistLocationsViewset),
    ("observations", views.ObservationsViewset),
    ("observedproperties", views.ObservedPropertiesViewset),
    ("pagcgaz", views.PagcGazViewset),
    ("pagclex", views.PagcLexViewset),
    ("pagcrules", views.PagcRulesViewset),
    ("place", views.PlaceViewset),
    ("placelookup", views.PlaceLookupViewset),
    ("preparationprocedures", views.PreparationProceduresViewset),
    ("preparationsteps", views.PreparationStepsViewset),
    ("relateddatastreams", views.RelatedDatastreamsViewset),
    ("relatedfeatures", views.RelatedFeaturesViewset),
    ("relatedobservations", views.RelatedObservationsViewset),
    ("relatedthings", views.RelatedThingsViewset),
    ("relationroles", views.RelationRolesViewset),
    ("samplersamplingprocedure", views.SamplerSamplingProcedureViewset),
    ("samplers", views.SamplersViewset),
    ("samplingprocedures", views.SamplingProceduresViewset),
    ("samplings", views.SamplingsViewset),
    ("secondaryunitlookup", views.SecondaryUnitLookupViewset),
    ("sensors", views.SensorsViewset),
    ("state", views.StateViewset),
    ("statelookup", views.StateLookupViewset),
    ("streettypelookup", views.StreetTypeLookupViewset),
    ("tabblock", views.TabblockViewset),
    ("tabblock20", views.Tabblock20Viewset),
    ("things", views.ThingsViewset),
    ("thingslocations", views.ThingsLocationsViewset),
    ("topology", views.TopologyViewset),
    ("tract", views.TractViewset),
    ("zcta5", views.Zcta5Viewset),
    ("ziplookup", views.ZipLookupViewset),
    ("ziplookupall", views.ZipLookupAllViewset),
    ("ziplookupbase", views.ZipLookupBaseViewset),
    ("zipstate", views.ZipStateViewset),
    ("zipstateloc", views.ZipStateLocViewset),
]


# ===================================================================
# 2.  set_filterset_fields_exclude helper
# ===================================================================
class SetFiltersetFieldsExcludeTests(SimpleTestCase):
    """Verify the helper correctly excludes unsupported field types."""

    def test_excludes_json_fields(self):
        """JSONField should be excluded from filterset fields."""
        fields = set_filterset_fields_exclude(serializers.ThingsSerializer)
        self.assertNotIn("properties", fields)

    def test_excludes_geometry_fields(self):
        """GeometryField & subclasses should be excluded."""
        fields = set_filterset_fields_exclude(serializers.LocationsSerializer)
        self.assertNotIn("geom", fields)

    def test_excludes_foreign_keys(self):
        """ForeignKey fields should be excluded."""
        fields = set_filterset_fields_exclude(serializers.DatastreamsSerializer)
        self.assertNotIn("sensor", fields)
        self.assertNotIn("thing", fields)

    def test_excludes_composite_primary_key(self):
        """CompositePrimaryKey fields should be excluded."""
        fields = set_filterset_fields_exclude(serializers.ThingsLocationsSerializer)
        self.assertNotIn("pk", fields)

    def test_includes_text_fields(self):
        """Regular text fields should be included."""
        fields = set_filterset_fields_exclude(serializers.ThingsSerializer)
        self.assertIn("name", fields)
        self.assertIn("description", fields)
        self.assertIn("definition", fields)

    def test_includes_id_for_simple_pk(self):
        """PositiveBigIntegerField PK should be included."""
        fields = set_filterset_fields_exclude(serializers.ThingsSerializer)
        self.assertIn("id", fields)

    def test_returns_list(self):
        result = set_filterset_fields_exclude(serializers.SensorsSerializer)
        self.assertIsInstance(result, list)


# ===================================================================
# 3.  MetaViewset configuration
# ===================================================================
class MetaViewsetConfigTests(SimpleTestCase):
    """Verify the base viewset is configured correctly."""

    def test_permission_classes(self):
        self.assertEqual(
            MetaViewset.permission_classes,
            [permissions.IsAuthenticatedOrReadOnly],
        )

    def test_filter_backends_count(self):
        self.assertEqual(len(MetaViewset.filter_backends), 3)

    def test_filter_backends_contains_django_filter(self):
        from django_filters.rest_framework import DjangoFilterBackend

        self.assertIn(DjangoFilterBackend, MetaViewset.filter_backends)

    def test_filter_backends_contains_search_filter(self):
        from rest_framework.filters import SearchFilter

        self.assertIn(SearchFilter, MetaViewset.filter_backends)

    def test_filter_backends_contains_ordering_filter(self):
        from rest_framework.filters import OrderingFilter

        self.assertIn(OrderingFilter, MetaViewset.filter_backends)

    def test_serializer_class_is_none_on_base(self):
        self.assertIsNone(MetaViewset.serializer_class)


# ===================================================================
# 4.  URL routing
# ===================================================================
class URLRoutingTests(SimpleTestCase):
    """Verify that all expected API routes are resolvable."""

    def test_swagger_url_resolves(self):
        url = reverse("swagger")
        self.assertEqual(url, "/api/swagger/")

    def test_schema_url_resolves(self):
        url = reverse("schema")
        self.assertEqual(url, "/api/schema/")

    def test_jwt_obtain_url_resolves(self):
        url = reverse("jwt")
        self.assertEqual(url, "/api/jwt//")

    def test_jwt_verify_url_resolves(self):
        url = reverse("jwt_verify")
        self.assertEqual(url, "/api/jwt/verify/")

    def test_jwt_refresh_url_resolves(self):
        url = reverse("jwt_refresh")
        self.assertEqual(url, "/api/jwt/refresh/")

    def test_all_api_list_routes_resolve(self):
        """Every registered viewset should have a resolvable list URL."""
        for basename, _ in VIEWSET_REGISTRY:
            with self.subTest(basename=basename):
                url = reverse(f"{basename}-list")
                self.assertTrue(
                    url.startswith("/api/sensorthings/"),
                    f"Expected /api/sensorthings/ prefix, got {url}",
                )

    def test_all_api_detail_routes_resolve(self):
        """Every registered viewset should have a resolvable detail URL."""
        for basename, _ in VIEWSET_REGISTRY:
            with self.subTest(basename=basename):
                url = reverse(f"{basename}-detail", kwargs={"pk": 1})
                self.assertIn("/1/", url)


# ===================================================================
# 5.  Anonymous access (read-only)
# ===================================================================
@override_settings(
    SENSORTHINGS_ENABLE_PUBLIC_PRIVATE=False,
    SENSORTHINGS_ENABLE_OWNER=False,
)
class AnonymousAccessTests(SimpleTestCase):
    """Unauthenticated users should not be able to write."""

    def setUp(self):
        self.client = APIClient()

    def test_anonymous_post_returns_403(self):
        """POST to any endpoint should be forbidden for anonymous users."""
        url = reverse("things-list")
        response = self.client.post(url, {}, format="json")
        self.assertIn(response.status_code, (401, 403))

    def test_anonymous_put_returns_403(self):
        url = reverse("things-detail", kwargs={"pk": 1})
        response = self.client.put(url, {}, format="json")
        self.assertIn(response.status_code, (401, 403))

    def test_anonymous_delete_returns_403(self):
        url = reverse("things-detail", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertIn(response.status_code, (401, 403))


# ===================================================================
# 6.  Serializer ↔ Model mapping
# ===================================================================
SERIALIZER_MODEL_PAIRS = [
    (serializers.ThingsSerializer, models.Things),
    (serializers.SensorsSerializer, models.Sensors),
    (serializers.DatastreamsSerializer, models.Datastreams),
    (serializers.ObservationsSerializer, models.Observations),
    (serializers.FeaturesSerializer, models.Features),
    (serializers.LocationsSerializer, models.Locations),
    (serializers.ObservedPropertiesSerializer, models.ObservedProperties),
    (serializers.HistLocationsSerializer, models.HistLocations),
    (serializers.FeatureTypesSerializer, models.FeatureTypes),
    (serializers.SamplingsSerializer, models.Samplings),
    (serializers.SamplersSerializer, models.Samplers),
    (serializers.SamplingProceduresSerializer, models.SamplingProcedures),
    (serializers.PreparationProceduresSerializer, models.PreparationProcedures),
    (serializers.PreparationStepsSerializer, models.PreparationSteps),
    (serializers.RelationRolesSerializer, models.RelationRoles),
    (serializers.RelatedDatastreamsSerializer, models.RelatedDatastreams),
    (serializers.RelatedFeaturesSerializer, models.RelatedFeatures),
    (serializers.RelatedObservationsSerializer, models.RelatedObservations),
    (serializers.RelatedThingsSerializer, models.RelatedThings),
    (serializers.ThingsLocationsSerializer, models.ThingsLocations),
    (serializers.LocationsHistLocationsSerializer, models.LocationsHistLocations),
    (
        serializers.DatastreamsObservedPropertiesSerializer,
        models.DatastreamsObservedProperties,
    ),
    (
        serializers.DatastreamsFeaturesUltimateSerializer,
        models.DatastreamsFeaturesUltimate,
    ),
    (serializers.FeaturesFeatureTypesSerializer, models.FeaturesFeatureTypes),
    (serializers.SamplerSamplingProcedureSerializer, models.SamplerSamplingProcedure),
]


class SerializerModelMappingTests(SimpleTestCase):
    """Each serializer must reference the correct model and expose all fields."""

    def test_serializer_model_matches(self):
        for ser_cls, model_cls in SERIALIZER_MODEL_PAIRS:
            with self.subTest(serializer=ser_cls.__name__):
                self.assertEqual(
                    ser_cls.Meta.model,
                    model_cls,
                    f"{ser_cls.__name__}.Meta.model != {model_cls.__name__}",
                )

    def test_serializer_fields_all(self):
        for ser_cls, _ in SERIALIZER_MODEL_PAIRS:
            with self.subTest(serializer=ser_cls.__name__):
                self.assertEqual(
                    ser_cls.Meta.fields,
                    "__all__",
                    f"{ser_cls.__name__}.Meta.fields should be '__all__'",
                )


# ===================================================================
# 7.  Viewset ↔ Serializer mapping
# ===================================================================
VIEWSET_SERIALIZER_PAIRS = [
    (views.ThingsViewset, serializers.ThingsSerializer),
    (views.SensorsViewset, serializers.SensorsSerializer),
    (views.DatastreamsViewset, serializers.DatastreamsSerializer),
    (views.ObservationsViewset, serializers.ObservationsSerializer),
    (views.FeaturesViewset, serializers.FeaturesSerializer),
    (views.LocationsViewset, serializers.LocationsSerializer),
    (views.ObservedPropertiesViewset, serializers.ObservedPropertiesSerializer),
    (views.HistLocationsViewset, serializers.HistLocationsSerializer),
    (views.SamplingsViewset, serializers.SamplingsSerializer),
    (views.SamplersViewset, serializers.SamplersSerializer),
    (views.RelationRolesViewset, serializers.RelationRolesSerializer),
    (views.TopologyViewset, serializers.TopologySerializer),
    (views.AddrViewset, serializers.AddrSerializer),
    (views.CountyViewset, serializers.CountySerializer),
    (views.StateViewset, serializers.StateSerializer),
    (views.PlaceViewset, serializers.PlaceSerializer),
    (views.EdgesViewset, serializers.EdgesSerializer),
    (views.FacesViewset, serializers.FacesSerializer),
]


class ViewsetSerializerMappingTests(SimpleTestCase):
    """Each viewset must reference the correct serializer."""

    def test_viewset_serializer_matches(self):
        for vs_cls, ser_cls in VIEWSET_SERIALIZER_PAIRS:
            with self.subTest(viewset=vs_cls.__name__):
                self.assertEqual(
                    vs_cls.serializer_class,
                    ser_cls,
                    f"{vs_cls.__name__}.serializer_class != {ser_cls.__name__}",
                )


# ===================================================================
# 8.  APIClient CRUD actions against the database
# ===================================================================
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CRUDTestMixin:
    """Mixin providing helpers for CRUD API tests.

    Subclasses must define:
        - ``list_url_name``: e.g. ``"things-list"``
        - ``detail_url_name``: e.g. ``"things-detail"``
        - ``create_payload``: dict for POST
        - ``update_payload``: dict for full PUT
        - ``patch_payload``: dict for partial PATCH
        - ``patch_field``: the field name to verify after PATCH
        - ``patch_expected``: the expected value after PATCH
    """

    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(
            username="admin", password="admin123", email="admin@test.com"
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.superuser)

    def get_list_url(self):
        return reverse(self.list_url_name)

    def get_detail_url(self, pk):
        return reverse(self.detail_url_name, kwargs={"pk": pk})

    # -- Create --
    def test_create(self):
        url = self.get_list_url()
        response = self.client.post(url, self.create_payload, format="json")
        self.assertEqual(response.status_code, 201, response.data)

    # -- List --
    def test_list(self):
        # Ensure at least one object exists
        self.client.post(self.get_list_url(), self.create_payload, format="json")
        response = self.client.get(self.get_list_url())
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    # -- Retrieve --
    def test_retrieve(self):
        create_resp = self.client.post(
            self.get_list_url(), self.create_payload, format="json"
        )
        pk = create_resp.data["id"]
        response = self.client.get(self.get_detail_url(pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], pk)

    # -- Update (PUT) --
    def test_update(self):
        create_resp = self.client.post(
            self.get_list_url(), self.create_payload, format="json"
        )
        pk = create_resp.data["id"]
        response = self.client.put(
            self.get_detail_url(pk), self.update_payload, format="json"
        )
        self.assertEqual(response.status_code, 200, response.data)

    # -- Partial Update (PATCH) --
    def test_partial_update(self):
        create_resp = self.client.post(
            self.get_list_url(), self.create_payload, format="json"
        )
        pk = create_resp.data["id"]
        response = self.client.patch(
            self.get_detail_url(pk), self.patch_payload, format="json"
        )
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data[self.patch_field], self.patch_expected)

    # -- Delete --
    def test_delete(self):
        create_resp = self.client.post(
            self.get_list_url(), self.create_payload, format="json"
        )
        pk = create_resp.data["id"]
        response = self.client.delete(self.get_detail_url(pk))
        self.assertEqual(response.status_code, 204)
        # Confirm gone
        response = self.client.get(self.get_detail_url(pk))
        self.assertEqual(response.status_code, 404)


@override_settings(
    SENSORTHINGS_ENABLE_PUBLIC_PRIVATE=False,
    SENSORTHINGS_ENABLE_OWNER=False,
)
class ThingsCRUDTests(CRUDTestMixin, TestCase):
    list_url_name = "things-list"
    detail_url_name = "things-detail"
    create_payload = {
        "id": 1,
        "name": "Weather Station A",
        "definition": "A weather station",
        "description": "Outdoor weather station",
    }
    update_payload = {
        "id": 1,
        "name": "Weather Station B",
        "definition": "Updated definition",
        "description": "Updated description",
    }
    patch_payload = {"name": "Patched Station"}
    patch_field = "name"
    patch_expected = "Patched Station"


@override_settings(
    SENSORTHINGS_ENABLE_PUBLIC_PRIVATE=False,
    SENSORTHINGS_ENABLE_OWNER=False,
)
class SensorsCRUDTests(CRUDTestMixin, TestCase):
    list_url_name = "sensors-list"
    detail_url_name = "sensors-detail"
    create_payload = {
        "id": 1,
        "name": "Temperature Sensor",
        "definition": "Measures temperature",
        "description": "PT100 sensor",
        "encoding_type": "application/json",
    }
    update_payload = {
        "id": 1,
        "name": "Humidity Sensor",
        "definition": "Measures humidity",
        "description": "Capacitive sensor",
        "encoding_type": "application/json",
    }
    patch_payload = {"description": "Patched description"}
    patch_field = "description"
    patch_expected = "Patched description"


@override_settings(
    SENSORTHINGS_ENABLE_PUBLIC_PRIVATE=False,
    SENSORTHINGS_ENABLE_OWNER=False,
)
class ObservedPropertiesCRUDTests(CRUDTestMixin, TestCase):
    list_url_name = "observedproperties-list"
    detail_url_name = "observedproperties-detail"
    create_payload = {
        "id": 1,
        "name": "Temperature",
        "definition": "Air temperature in Celsius",
        "description": "Ambient air temperature",
    }
    update_payload = {
        "id": 1,
        "name": "Humidity",
        "definition": "Relative humidity in %",
        "description": "Ambient humidity",
    }
    patch_payload = {"name": "Air Pressure"}
    patch_field = "name"
    patch_expected = "Air Pressure"


@override_settings(
    SENSORTHINGS_ENABLE_PUBLIC_PRIVATE=False,
    SENSORTHINGS_ENABLE_OWNER=False,
)
class FeatureTypesCRUDTests(CRUDTestMixin, TestCase):
    list_url_name = "featuretypes-list"
    detail_url_name = "featuretypes-detail"
    create_payload = {
        "id": 1,
        "name": "Point",
        "definition": "A point location",
        "description": "Geographic point",
    }
    update_payload = {
        "id": 1,
        "name": "Polygon",
        "definition": "A polygon area",
        "description": "Geographic polygon",
    }
    patch_payload = {"definition": "Patched definition"}
    patch_field = "definition"
    patch_expected = "Patched definition"


@override_settings(
    SENSORTHINGS_ENABLE_PUBLIC_PRIVATE=False,
    SENSORTHINGS_ENABLE_OWNER=False,
)
class RelationRolesCRUDTests(CRUDTestMixin, TestCase):
    list_url_name = "relationroles-list"
    detail_url_name = "relationroles-detail"
    create_payload = {
        "id": 1,
        "name": "parent",
        "definition": "Parent relationship",
        "inverse_name": "child",
        "inverse_definition": "Child relationship",
        "description": "Hierarchical relation",
    }
    update_payload = {
        "id": 1,
        "name": "sibling",
        "definition": "Sibling relationship",
        "inverse_name": "sibling",
        "inverse_definition": "Sibling relationship",
        "description": "Peer relation",
    }
    patch_payload = {"name": "contains"}
    patch_field = "name"
    patch_expected = "contains"


@override_settings(
    SENSORTHINGS_ENABLE_PUBLIC_PRIVATE=False,
    SENSORTHINGS_ENABLE_OWNER=False,
)
class SamplingProceduresCRUDTests(CRUDTestMixin, TestCase):
    list_url_name = "samplingprocedures-list"
    detail_url_name = "samplingprocedures-detail"
    create_payload = {
        "id": 1,
        "name": "Grab Sample",
        "definition": "Single grab sample procedure",
        "description": "Manual grab sample",
    }
    update_payload = {
        "id": 1,
        "name": "Composite Sample",
        "definition": "Time-weighted composite",
        "description": "Automated composite",
    }
    patch_payload = {"description": "Patched procedure"}
    patch_field = "description"
    patch_expected = "Patched procedure"


@override_settings(
    SENSORTHINGS_ENABLE_PUBLIC_PRIVATE=False,
    SENSORTHINGS_ENABLE_OWNER=False,
)
class PreparationProceduresCRUDTests(CRUDTestMixin, TestCase):
    list_url_name = "preparationprocedures-list"
    detail_url_name = "preparationprocedures-detail"
    create_payload = {
        "id": 1,
        "name": "Filtration",
        "definition": "Filter sample through 0.45μm",
        "description": "Standard filtration prep",
    }
    update_payload = {
        "id": 1,
        "name": "Acidification",
        "definition": "Add HNO3 to pH < 2",
        "description": "Standard acid preservation",
    }
    patch_payload = {"name": "Centrifuge"}
    patch_field = "name"
    patch_expected = "Centrifuge"


@override_settings(
    SENSORTHINGS_ENABLE_PUBLIC_PRIVATE=False,
    SENSORTHINGS_ENABLE_OWNER=False,
)
class DatastreamsCRUDTests(TestCase):
    """CRUD tests for Datastreams (requires Sensor + Thing FK)."""

    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(
            username="admin", password="admin123", email="admin@test.com"
        )
        cls.sensor = models.Sensors.objects.create(
            id=1, name="Temp Sensor", description="Temperature"
        )
        cls.thing = models.Things.objects.create(
            id=1, name="Station 1", description="Weather station"
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.superuser)

    def test_create(self):
        url = reverse("datastreams-list")
        payload = {
            "id": 1,
            "sensor": self.sensor.id,
            "thing": self.thing.id,
            "name": "Temperature Stream",
            "description": "Temperature data stream",
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, 201, response.data)

    def test_list(self):
        models.Datastreams.objects.create(
            id=2, sensor=self.sensor, thing=self.thing, name="Stream"
        )
        response = self.client.get(reverse("datastreams-list"))
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_retrieve(self):
        ds = models.Datastreams.objects.create(
            id=3, sensor=self.sensor, thing=self.thing, name="Stream 3"
        )
        response = self.client.get(reverse("datastreams-detail", kwargs={"pk": ds.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Stream 3")

    def test_update(self):
        ds = models.Datastreams.objects.create(
            id=4, sensor=self.sensor, thing=self.thing, name="Stream 4"
        )
        payload = {
            "id": 4,
            "sensor": self.sensor.id,
            "thing": self.thing.id,
            "name": "Updated Stream",
            "description": "Updated",
        }
        response = self.client.put(
            reverse("datastreams-detail", kwargs={"pk": ds.id}),
            payload,
            format="json",
        )
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data["name"], "Updated Stream")

    def test_partial_update(self):
        ds = models.Datastreams.objects.create(
            id=5, sensor=self.sensor, thing=self.thing, name="Stream 5"
        )
        response = self.client.patch(
            reverse("datastreams-detail", kwargs={"pk": ds.id}),
            {"name": "Patched Stream"},
            format="json",
        )
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data["name"], "Patched Stream")

    def test_delete(self):
        ds = models.Datastreams.objects.create(
            id=6, sensor=self.sensor, thing=self.thing, name="Stream 6"
        )
        response = self.client.delete(
            reverse("datastreams-detail", kwargs={"pk": ds.id})
        )
        self.assertEqual(response.status_code, 204)
        self.assertFalse(models.Datastreams.objects.filter(pk=ds.id).exists())
