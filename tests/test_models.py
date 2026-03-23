from sensorthings import models
from django.test import SimpleTestCase, TestCase


class MetaModelTests(SimpleTestCase):
    """Tests for the abstract MetaModel base class."""

    def test_meta_model_is_abstract(self):
        self.assertTrue(models.MetaModel._meta.abstract)


class AddrTests(TestCase):
    def test_meta(self):
        self.assertEqual(models.Addr._meta.db_table, "addr")
        self.assertFalse(models.Addr._meta.abstract)

    def test_fields(self):
        field_names = [f.name for f in models.Addr._meta.get_fields()]
        for expected in ["gid", "tlid", "fromhn", "tohn", "side", "zip", "statefp"]:
            self.assertIn(expected, field_names)

    def test_create_read_update_delete(self):
        """CRUD test instance"""
        # create
        instance = models.Addr.objects.create(zip="12345", statefp="NY")

        # read
        fetched = models.Addr.objects.get(pk=instance.pk)
        self.assertEqual(fetched.zip, "12345")
        self.assertEqual(fetched.statefp, "NY")

        # update
        fetched.zip = "67890"
        fetched.save()
        updated = models.Addr.objects.get(pk=instance.pk)
        self.assertEqual(updated.zip, "67890")

        # delete
        pk = instance.pk
        instance.delete()
        self.assertFalse(models.Addr.objects.filter(pk=pk).exists())


class AddrfeatTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Addrfeat._meta.db_table, "addrfeat")

    def test_fields(self):
        field_names = [f.name for f in models.Addrfeat._meta.get_fields()]
        for expected in ["statefp", "linearid", "fullname", "the_geom"]:
            self.assertIn(expected, field_names)


class BgTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Bg._meta.db_table, "bg")

    def test_fields(self):
        field_names = [f.name for f in models.Bg._meta.get_fields()]
        for expected in ["statefp", "countyfp", "tractce", "blkgrpce", "the_geom"]:
            self.assertIn(expected, field_names)


class CountyTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.County._meta.db_table, "county")

    def test_fields(self):
        field_names = [f.name for f in models.County._meta.get_fields()]
        for expected in ["statefp", "countyfp", "name", "the_geom"]:
            self.assertIn(expected, field_names)


class CountyLookupTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.CountyLookup._meta.db_table, "county_lookup")

    def test_fields(self):
        field_names = [f.name for f in models.CountyLookup._meta.get_fields()]
        for expected in ["st_code", "state", "co_code", "name"]:
            self.assertIn(expected, field_names)


class CountysubLookupTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.CountysubLookup._meta.db_table, "countysub_lookup")

    def test_fields(self):
        field_names = [f.name for f in models.CountysubLookup._meta.get_fields()]
        for expected in ["st_code", "state", "co_code", "county", "cs_code", "name"]:
            self.assertIn(expected, field_names)


class CousubTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Cousub._meta.db_table, "cousub")

    def test_fields(self):
        field_names = [f.name for f in models.Cousub._meta.get_fields()]
        for expected in ["statefp", "countyfp", "cousubfp", "name", "the_geom"]:
            self.assertIn(expected, field_names)


class DatabasechangelogTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Databasechangelog._meta.db_table, "databasechangelog")

    def test_fields(self):
        field_names = [f.name for f in models.Databasechangelog._meta.get_fields()]
        for expected in ["id", "author", "filename", "dateexecuted", "exectype"]:
            self.assertIn(expected, field_names)


class DatabasechangeloglockTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.Databasechangeloglock._meta.db_table, "databasechangeloglock"
        )

    def test_fields(self):
        field_names = [f.name for f in models.Databasechangeloglock._meta.get_fields()]
        for expected in ["id", "locked", "lockgranted", "lockedby"]:
            self.assertIn(expected, field_names)


class DatastreamsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Datastreams._meta.db_table, "datastreams")

    def test_fields(self):
        field_names = [f.name for f in models.Datastreams._meta.get_fields()]
        for expected in ["id", "sensor", "thing", "name", "description", "properties"]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.Datastreams._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model")
        }
        self.assertEqual(fk_fields["sensor"], models.Sensors)
        self.assertEqual(fk_fields["thing"], models.Things)


class DatastreamsFeaturesUltimateTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.DatastreamsFeaturesUltimate._meta.db_table,
            "datastreams_features_ultimate",
        )

    def test_fields(self):
        field_names = [
            f.name for f in models.DatastreamsFeaturesUltimate._meta.get_fields()
        ]
        for expected in ["datastream", "feature"]:
            self.assertIn(expected, field_names)


class DatastreamsObservedPropertiesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.DatastreamsObservedProperties._meta.db_table,
            "datastreams_observed_properties",
        )

    def test_fields(self):
        field_names = [
            f.name for f in models.DatastreamsObservedProperties._meta.get_fields()
        ]
        for expected in ["observed_property", "datastream"]:
            self.assertIn(expected, field_names)


class DirectionLookupTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.DirectionLookup._meta.db_table, "direction_lookup")

    def test_fields(self):
        field_names = [f.name for f in models.DirectionLookup._meta.get_fields()]
        for expected in ["name", "abbrev"]:
            self.assertIn(expected, field_names)


class EdgesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Edges._meta.db_table, "edges")

    def test_fields(self):
        field_names = [f.name for f in models.Edges._meta.get_fields()]
        for expected in ["statefp", "tlid", "fullname", "the_geom"]:
            self.assertIn(expected, field_names)


class FacesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Faces._meta.db_table, "faces")

    def test_fields(self):
        field_names = [f.name for f in models.Faces._meta.get_fields()]
        for expected in ["statefp", "countyfp", "the_geom"]:
            self.assertIn(expected, field_names)


class FeatnamesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Featnames._meta.db_table, "featnames")

    def test_fields(self):
        field_names = [f.name for f in models.Featnames._meta.get_fields()]
        for expected in ["tlid", "fullname", "name", "linearid"]:
            self.assertIn(expected, field_names)


class FeatureTypesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.FeatureTypes._meta.db_table, "feature_types")

    def test_fields(self):
        field_names = [f.name for f in models.FeatureTypes._meta.get_fields()]
        for expected in ["id", "name", "definition", "description", "properties"]:
            self.assertIn(expected, field_names)


class FeaturesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Features._meta.db_table, "features")

    def test_fields(self):
        field_names = [f.name for f in models.Features._meta.get_fields()]
        for expected in ["id", "name", "description", "geom", "properties"]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.Features._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model") and not f.auto_created
        }
        self.assertEqual(fk_fields["creator_sampling"], models.Samplings)


class FeaturesFeatureTypesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.FeaturesFeatureTypes._meta.db_table, "features_feature_types"
        )

    def test_fields(self):
        field_names = [f.name for f in models.FeaturesFeatureTypes._meta.get_fields()]
        for expected in ["feature", "feature_type"]:
            self.assertIn(expected, field_names)


class GeocodeSettingsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.GeocodeSettings._meta.db_table, "geocode_settings")

    def test_fields(self):
        field_names = [f.name for f in models.GeocodeSettings._meta.get_fields()]
        for expected in ["name", "setting", "unit", "category"]:
            self.assertIn(expected, field_names)


class GeocodeSettingsDefaultTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.GeocodeSettingsDefault._meta.db_table, "geocode_settings_default"
        )

    def test_fields(self):
        field_names = [f.name for f in models.GeocodeSettingsDefault._meta.get_fields()]
        for expected in ["name", "setting", "unit", "category"]:
            self.assertIn(expected, field_names)


class HistLocationsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.HistLocations._meta.db_table, "hist_locations")

    def test_fields(self):
        field_names = [f.name for f in models.HistLocations._meta.get_fields()]
        for expected in ["id", "thing", "time"]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.HistLocations._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model") and not f.auto_created
        }
        self.assertEqual(fk_fields["thing"], models.Things)


class LayerTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Layer._meta.db_table, "layer")

    def test_fields(self):
        field_names = [f.name for f in models.Layer._meta.get_fields()]
        for expected in ["topology", "layer_id", "schema_name", "table_name"]:
            self.assertIn(expected, field_names)


class LoaderLookuptablesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.LoaderLookuptables._meta.db_table, "loader_lookuptables"
        )

    def test_fields(self):
        field_names = [f.name for f in models.LoaderLookuptables._meta.get_fields()]
        for expected in ["process_order", "lookup_name", "table_name", "load"]:
            self.assertIn(expected, field_names)


class LoaderPlatformTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.LoaderPlatform._meta.db_table, "loader_platform")

    def test_fields(self):
        field_names = [f.name for f in models.LoaderPlatform._meta.get_fields()]
        for expected in ["os", "declare_sect", "pgbin", "wget"]:
            self.assertIn(expected, field_names)


class LoaderVariablesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.LoaderVariables._meta.db_table, "loader_variables")

    def test_fields(self):
        field_names = [f.name for f in models.LoaderVariables._meta.get_fields()]
        for expected in ["tiger_year", "website_root", "staging_fold"]:
            self.assertIn(expected, field_names)


class LocationsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Locations._meta.db_table, "locations")

    def test_fields(self):
        field_names = [f.name for f in models.Locations._meta.get_fields()]
        for expected in ["id", "name", "description", "geom", "properties"]:
            self.assertIn(expected, field_names)


class LocationsHistLocationsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.LocationsHistLocations._meta.db_table, "locations_hist_locations"
        )

    def test_fields(self):
        field_names = [f.name for f in models.LocationsHistLocations._meta.get_fields()]
        for expected in ["location", "hist_location"]:
            self.assertIn(expected, field_names)


class ObservationsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Observations._meta.db_table, "observations")

    def test_fields(self):
        field_names = [f.name for f in models.Observations._meta.get_fields()]
        for expected in [
            "id",
            "datastream",
            "feature",
            "result_number",
            "result_boolean",
            "properties",
        ]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.Observations._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model") and not f.auto_created
        }
        self.assertEqual(fk_fields["datastream"], models.Datastreams)
        self.assertEqual(fk_fields["feature"], models.Features)


class ObservedPropertiesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.ObservedProperties._meta.db_table, "observed_properties"
        )

    def test_fields(self):
        field_names = [f.name for f in models.ObservedProperties._meta.get_fields()]
        for expected in ["id", "name", "definition", "description", "properties"]:
            self.assertIn(expected, field_names)


class PagcGazTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.PagcGaz._meta.db_table, "pagc_gaz")

    def test_fields(self):
        field_names = [f.name for f in models.PagcGaz._meta.get_fields()]
        for expected in ["seq", "word", "stdword", "token", "is_custom"]:
            self.assertIn(expected, field_names)


class PagcLexTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.PagcLex._meta.db_table, "pagc_lex")

    def test_fields(self):
        field_names = [f.name for f in models.PagcLex._meta.get_fields()]
        for expected in ["seq", "word", "stdword", "token", "is_custom"]:
            self.assertIn(expected, field_names)


class PagcRulesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.PagcRules._meta.db_table, "pagc_rules")

    def test_fields(self):
        field_names = [f.name for f in models.PagcRules._meta.get_fields()]
        for expected in ["rule", "is_custom"]:
            self.assertIn(expected, field_names)


class PlaceTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Place._meta.db_table, "place")

    def test_fields(self):
        field_names = [f.name for f in models.Place._meta.get_fields()]
        for expected in ["statefp", "placefp", "name", "the_geom"]:
            self.assertIn(expected, field_names)


class PlaceLookupTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.PlaceLookup._meta.db_table, "place_lookup")

    def test_fields(self):
        field_names = [f.name for f in models.PlaceLookup._meta.get_fields()]
        for expected in ["st_code", "state", "pl_code", "name"]:
            self.assertIn(expected, field_names)


class PreparationProceduresTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.PreparationProcedures._meta.db_table, "preparation_procedures"
        )

    def test_fields(self):
        field_names = [f.name for f in models.PreparationProcedures._meta.get_fields()]
        for expected in ["id", "name", "definition", "description", "properties"]:
            self.assertIn(expected, field_names)


class PreparationStepsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.PreparationSteps._meta.db_table, "preparation_steps")

    def test_fields(self):
        field_names = [f.name for f in models.PreparationSteps._meta.get_fields()]
        for expected in ["id", "feature", "preparation_procedure", "name", "time"]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.PreparationSteps._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model") and not f.auto_created
        }
        self.assertEqual(fk_fields["feature"], models.Features)
        self.assertEqual(
            fk_fields["preparation_procedure"], models.PreparationProcedures
        )


class RelatedDatastreamsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.RelatedDatastreams._meta.db_table, "related_datastreams"
        )

    def test_fields(self):
        field_names = [f.name for f in models.RelatedDatastreams._meta.get_fields()]
        for expected in [
            "id",
            "source_datastream",
            "target_datastream",
            "relation_role",
        ]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.RelatedDatastreams._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model") and not f.auto_created
        }
        self.assertEqual(fk_fields["source_datastream"], models.Datastreams)
        self.assertEqual(fk_fields["target_datastream"], models.Datastreams)
        self.assertEqual(fk_fields["relation_role"], models.RelationRoles)


class RelatedFeaturesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.RelatedFeatures._meta.db_table, "related_features")

    def test_fields(self):
        field_names = [f.name for f in models.RelatedFeatures._meta.get_fields()]
        for expected in ["id", "source_feature", "target_feature", "relation_role"]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.RelatedFeatures._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model") and not f.auto_created
        }
        self.assertEqual(fk_fields["source_feature"], models.Features)
        self.assertEqual(fk_fields["target_feature"], models.Features)
        self.assertEqual(fk_fields["relation_role"], models.RelationRoles)


class RelatedObservationsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.RelatedObservations._meta.db_table, "related_observations"
        )

    def test_fields(self):
        field_names = [f.name for f in models.RelatedObservations._meta.get_fields()]
        for expected in [
            "id",
            "source_observation",
            "target_observation",
            "relation_role",
        ]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.RelatedObservations._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model") and not f.auto_created
        }
        self.assertEqual(fk_fields["source_observation"], models.Observations)
        self.assertEqual(fk_fields["target_observation"], models.Observations)
        self.assertEqual(fk_fields["relation_role"], models.RelationRoles)


class RelatedThingsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.RelatedThings._meta.db_table, "related_things")

    def test_fields(self):
        field_names = [f.name for f in models.RelatedThings._meta.get_fields()]
        for expected in ["id", "source_thing", "target_thing", "relation_role"]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.RelatedThings._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model") and not f.auto_created
        }
        self.assertEqual(fk_fields["source_thing"], models.Things)
        self.assertEqual(fk_fields["target_thing"], models.Things)
        self.assertEqual(fk_fields["relation_role"], models.RelationRoles)


class RelationRolesTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.RelationRoles._meta.db_table, "relation_roles")

    def test_fields(self):
        field_names = [f.name for f in models.RelationRoles._meta.get_fields()]
        for expected in [
            "id",
            "name",
            "definition",
            "inverse_name",
            "description",
            "properties",
        ]:
            self.assertIn(expected, field_names)


class SamplerSamplingProcedureTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.SamplerSamplingProcedure._meta.db_table, "sampler_sampling_procedure"
        )

    def test_fields(self):
        field_names = [
            f.name for f in models.SamplerSamplingProcedure._meta.get_fields()
        ]
        for expected in ["sampler", "procedure"]:
            self.assertIn(expected, field_names)


class SamplersTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Samplers._meta.db_table, "samplers")

    def test_fields(self):
        field_names = [f.name for f in models.Samplers._meta.get_fields()]
        for expected in ["id", "name", "definition", "description", "sampler_type"]:
            self.assertIn(expected, field_names)


class SamplingProceduresTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.SamplingProcedures._meta.db_table, "sampling_procedures"
        )

    def test_fields(self):
        field_names = [f.name for f in models.SamplingProcedures._meta.get_fields()]
        for expected in ["id", "name", "definition", "description", "properties"]:
            self.assertIn(expected, field_names)


class SamplingsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Samplings._meta.db_table, "samplings")

    def test_fields(self):
        field_names = [f.name for f in models.Samplings._meta.get_fields()]
        for expected in [
            "id",
            "thing",
            "sampled_feature",
            "sampler",
            "procedure",
            "name",
            "geom",
        ]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.Samplings._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model") and not f.auto_created
        }
        self.assertEqual(fk_fields["thing"], models.Things)
        self.assertEqual(fk_fields["sampled_feature"], models.Features)
        self.assertEqual(fk_fields["sampler"], models.Samplers)
        self.assertEqual(fk_fields["procedure"], models.SamplingProcedures)


class SecondaryUnitLookupTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(
            models.SecondaryUnitLookup._meta.db_table, "secondary_unit_lookup"
        )

    def test_fields(self):
        field_names = [f.name for f in models.SecondaryUnitLookup._meta.get_fields()]
        for expected in ["name", "abbrev"]:
            self.assertIn(expected, field_names)


class SensorsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Sensors._meta.db_table, "sensors")

    def test_fields(self):
        field_names = [f.name for f in models.Sensors._meta.get_fields()]
        for expected in [
            "id",
            "name",
            "definition",
            "description",
            "encoding_type",
            "metadata",
            "properties",
        ]:
            self.assertIn(expected, field_names)


class StateTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.State._meta.db_table, "state")

    def test_fields(self):
        field_names = [f.name for f in models.State._meta.get_fields()]
        for expected in ["statefp", "stusps", "name", "the_geom"]:
            self.assertIn(expected, field_names)


class StateLookupTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.StateLookup._meta.db_table, "state_lookup")

    def test_fields(self):
        field_names = [f.name for f in models.StateLookup._meta.get_fields()]
        for expected in ["st_code", "name", "abbrev", "statefp"]:
            self.assertIn(expected, field_names)


class StreetTypeLookupTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.StreetTypeLookup._meta.db_table, "street_type_lookup")

    def test_fields(self):
        field_names = [f.name for f in models.StreetTypeLookup._meta.get_fields()]
        for expected in ["name", "abbrev", "is_hw"]:
            self.assertIn(expected, field_names)


class TabblockTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Tabblock._meta.db_table, "tabblock")

    def test_fields(self):
        field_names = [f.name for f in models.Tabblock._meta.get_fields()]
        for expected in ["statefp", "countyfp", "tractce", "blockce", "the_geom"]:
            self.assertIn(expected, field_names)


class Tabblock20Tests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Tabblock20._meta.db_table, "tabblock20")

    def test_fields(self):
        field_names = [f.name for f in models.Tabblock20._meta.get_fields()]
        for expected in ["geoid", "statefp", "countyfp", "housing", "pop", "the_geom"]:
            self.assertIn(expected, field_names)


class ThingsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Things._meta.db_table, "things")

    def test_fields(self):
        field_names = [f.name for f in models.Things._meta.get_fields()]
        for expected in ["id", "name", "definition", "description", "properties"]:
            self.assertIn(expected, field_names)


class ThingsLocationsTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.ThingsLocations._meta.db_table, "things_locations")

    def test_fields(self):
        field_names = [f.name for f in models.ThingsLocations._meta.get_fields()]
        for expected in ["thing", "location"]:
            self.assertIn(expected, field_names)

    def test_foreign_keys(self):
        fk_fields = {
            f.name: f.related_model
            for f in models.ThingsLocations._meta.get_fields()
            if f.is_relation and hasattr(f, "related_model") and not f.auto_created
        }
        self.assertEqual(fk_fields["thing"], models.Things)
        self.assertEqual(fk_fields["location"], models.Locations)


class TopologyTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Topology._meta.db_table, "topology")

    def test_fields(self):
        field_names = [f.name for f in models.Topology._meta.get_fields()]
        for expected in ["id", "name", "srid", "precision", "hasz"]:
            self.assertIn(expected, field_names)


class TractTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Tract._meta.db_table, "tract")

    def test_fields(self):
        field_names = [f.name for f in models.Tract._meta.get_fields()]
        for expected in ["statefp", "countyfp", "tractce", "name", "the_geom"]:
            self.assertIn(expected, field_names)


class Zcta5Tests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.Zcta5._meta.db_table, "zcta5")

    def test_fields(self):
        field_names = [f.name for f in models.Zcta5._meta.get_fields()]
        for expected in ["statefp", "zcta5ce", "classfp", "the_geom"]:
            self.assertIn(expected, field_names)


class ZipLookupTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.ZipLookup._meta.db_table, "zip_lookup")

    def test_fields(self):
        field_names = [f.name for f in models.ZipLookup._meta.get_fields()]
        for expected in ["zip", "st_code", "state", "county", "place"]:
            self.assertIn(expected, field_names)


class ZipLookupAllTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.ZipLookupAll._meta.db_table, "zip_lookup_all")

    def test_fields(self):
        field_names = [f.name for f in models.ZipLookupAll._meta.get_fields()]
        for expected in ["zip", "st_code", "state", "county", "place"]:
            self.assertIn(expected, field_names)


class ZipLookupBaseTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.ZipLookupBase._meta.db_table, "zip_lookup_base")

    def test_fields(self):
        field_names = [f.name for f in models.ZipLookupBase._meta.get_fields()]
        for expected in ["zip", "state", "county", "city", "statefp"]:
            self.assertIn(expected, field_names)


class ZipStateTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.ZipState._meta.db_table, "zip_state")

    def test_fields(self):
        field_names = [f.name for f in models.ZipState._meta.get_fields()]
        for expected in ["zip", "stusps", "statefp"]:
            self.assertIn(expected, field_names)


class ZipStateLocTests(SimpleTestCase):
    def test_meta(self):
        self.assertEqual(models.ZipStateLoc._meta.db_table, "zip_state_loc")

    def test_fields(self):
        field_names = [f.name for f in models.ZipStateLoc._meta.get_fields()]
        for expected in ["zip", "stusps", "statefp", "place"]:
            self.assertIn(expected, field_names)
