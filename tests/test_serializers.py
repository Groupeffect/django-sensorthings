from django.test import SimpleTestCase
from sensorthings import models, serializers


class SerializerTests(SimpleTestCase):
    def test_addr_serializer(self):
        self.assertEqual(serializers.AddrSerializer.Meta.model, models.Addr)
        self.assertEqual(serializers.AddrSerializer.Meta.fields, "__all__")

    def test_addrfeat_serializer(self):
        self.assertEqual(serializers.AddrfeatSerializer.Meta.model, models.Addrfeat)
        self.assertEqual(serializers.AddrfeatSerializer.Meta.fields, "__all__")

    def test_bg_serializer(self):
        self.assertEqual(serializers.BgSerializer.Meta.model, models.Bg)
        self.assertEqual(serializers.BgSerializer.Meta.fields, "__all__")

    def test_county_serializer(self):
        self.assertEqual(serializers.CountySerializer.Meta.model, models.County)
        self.assertEqual(serializers.CountySerializer.Meta.fields, "__all__")

    def test_county_lookup_serializer(self):
        self.assertEqual(serializers.CountyLookupSerializer.Meta.model, models.CountyLookup)
        self.assertEqual(serializers.CountyLookupSerializer.Meta.fields, "__all__")

    def test_countysub_lookup_serializer(self):
        self.assertEqual(serializers.CountysubLookupSerializer.Meta.model, models.CountysubLookup)
        self.assertEqual(serializers.CountysubLookupSerializer.Meta.fields, "__all__")

    def test_cousub_serializer(self):
        self.assertEqual(serializers.CousubSerializer.Meta.model, models.Cousub)
        self.assertEqual(serializers.CousubSerializer.Meta.fields, "__all__")

    def test_databasechangelog_serializer(self):
        self.assertEqual(serializers.DatabasechangelogSerializer.Meta.model, models.Databasechangelog)
        self.assertEqual(serializers.DatabasechangelogSerializer.Meta.fields, "__all__")

    def test_databasechangeloglock_serializer(self):
        self.assertEqual(serializers.DatabasechangeloglockSerializer.Meta.model, models.Databasechangeloglock)
        self.assertEqual(serializers.DatabasechangeloglockSerializer.Meta.fields, "__all__")

    def test_datastreams_serializer(self):
        self.assertEqual(serializers.DatastreamsSerializer.Meta.model, models.Datastreams)
        self.assertEqual(serializers.DatastreamsSerializer.Meta.fields, "__all__")

    def test_datastreams_features_ultimate_serializer(self):
        self.assertEqual(serializers.DatastreamsFeaturesUltimateSerializer.Meta.model, models.DatastreamsFeaturesUltimate)
        self.assertEqual(serializers.DatastreamsFeaturesUltimateSerializer.Meta.fields, "__all__")

    def test_datastreams_observed_properties_serializer(self):
        self.assertEqual(serializers.DatastreamsObservedPropertiesSerializer.Meta.model, models.DatastreamsObservedProperties)
        self.assertEqual(serializers.DatastreamsObservedPropertiesSerializer.Meta.fields, "__all__")

    def test_direction_lookup_serializer(self):
        self.assertEqual(serializers.DirectionLookupSerializer.Meta.model, models.DirectionLookup)
        self.assertEqual(serializers.DirectionLookupSerializer.Meta.fields, "__all__")

    def test_edges_serializer(self):
        self.assertEqual(serializers.EdgesSerializer.Meta.model, models.Edges)
        self.assertEqual(serializers.EdgesSerializer.Meta.fields, "__all__")

    def test_faces_serializer(self):
        self.assertEqual(serializers.FacesSerializer.Meta.model, models.Faces)
        self.assertEqual(serializers.FacesSerializer.Meta.fields, "__all__")

    def test_featnames_serializer(self):
        self.assertEqual(serializers.FeatnamesSerializer.Meta.model, models.Featnames)
        self.assertEqual(serializers.FeatnamesSerializer.Meta.fields, "__all__")

    def test_feature_types_serializer(self):
        self.assertEqual(serializers.FeatureTypesSerializer.Meta.model, models.FeatureTypes)
        self.assertEqual(serializers.FeatureTypesSerializer.Meta.fields, "__all__")

    def test_features_serializer(self):
        self.assertEqual(serializers.FeaturesSerializer.Meta.model, models.Features)
        self.assertEqual(serializers.FeaturesSerializer.Meta.fields, "__all__")

    def test_features_feature_types_serializer(self):
        self.assertEqual(serializers.FeaturesFeatureTypesSerializer.Meta.model, models.FeaturesFeatureTypes)
        self.assertEqual(serializers.FeaturesFeatureTypesSerializer.Meta.fields, "__all__")

    def test_geocode_settings_serializer(self):
        self.assertEqual(serializers.GeocodeSettingsSerializer.Meta.model, models.GeocodeSettings)
        self.assertEqual(serializers.GeocodeSettingsSerializer.Meta.fields, "__all__")

    def test_geocode_settings_default_serializer(self):
        self.assertEqual(serializers.GeocodeSettingsDefaultSerializer.Meta.model, models.GeocodeSettingsDefault)
        self.assertEqual(serializers.GeocodeSettingsDefaultSerializer.Meta.fields, "__all__")

    def test_hist_locations_serializer(self):
        self.assertEqual(serializers.HistLocationsSerializer.Meta.model, models.HistLocations)
        self.assertEqual(serializers.HistLocationsSerializer.Meta.fields, "__all__")

    def test_layer_serializer(self):
        self.assertEqual(serializers.LayerSerializer.Meta.model, models.Layer)
        self.assertEqual(serializers.LayerSerializer.Meta.fields, "__all__")

    def test_loader_lookuptables_serializer(self):
        self.assertEqual(serializers.LoaderLookuptablesSerializer.Meta.model, models.LoaderLookuptables)
        self.assertEqual(serializers.LoaderLookuptablesSerializer.Meta.fields, "__all__")

    def test_loader_platform_serializer(self):
        self.assertEqual(serializers.LoaderPlatformSerializer.Meta.model, models.LoaderPlatform)
        self.assertEqual(serializers.LoaderPlatformSerializer.Meta.fields, "__all__")

    def test_loader_variables_serializer(self):
        self.assertEqual(serializers.LoaderVariablesSerializer.Meta.model, models.LoaderVariables)
        self.assertEqual(serializers.LoaderVariablesSerializer.Meta.fields, "__all__")

    def test_locations_serializer(self):
        self.assertEqual(serializers.LocationsSerializer.Meta.model, models.Locations)
        self.assertEqual(serializers.LocationsSerializer.Meta.fields, "__all__")

    def test_locations_hist_locations_serializer(self):
        self.assertEqual(serializers.LocationsHistLocationsSerializer.Meta.model, models.LocationsHistLocations)
        self.assertEqual(serializers.LocationsHistLocationsSerializer.Meta.fields, "__all__")

    def test_observations_serializer(self):
        self.assertEqual(serializers.ObservationsSerializer.Meta.model, models.Observations)
        self.assertEqual(serializers.ObservationsSerializer.Meta.fields, "__all__")

    def test_observed_properties_serializer(self):
        self.assertEqual(serializers.ObservedPropertiesSerializer.Meta.model, models.ObservedProperties)
        self.assertEqual(serializers.ObservedPropertiesSerializer.Meta.fields, "__all__")

    def test_pagc_gaz_serializer(self):
        self.assertEqual(serializers.PagcGazSerializer.Meta.model, models.PagcGaz)
        self.assertEqual(serializers.PagcGazSerializer.Meta.fields, "__all__")

    def test_pagc_lex_serializer(self):
        self.assertEqual(serializers.PagcLexSerializer.Meta.model, models.PagcLex)
        self.assertEqual(serializers.PagcLexSerializer.Meta.fields, "__all__")

    def test_pagc_rules_serializer(self):
        self.assertEqual(serializers.PagcRulesSerializer.Meta.model, models.PagcRules)
        self.assertEqual(serializers.PagcRulesSerializer.Meta.fields, "__all__")

    def test_place_serializer(self):
        self.assertEqual(serializers.PlaceSerializer.Meta.model, models.Place)
        self.assertEqual(serializers.PlaceSerializer.Meta.fields, "__all__")

    def test_place_lookup_serializer(self):
        self.assertEqual(serializers.PlaceLookupSerializer.Meta.model, models.PlaceLookup)
        self.assertEqual(serializers.PlaceLookupSerializer.Meta.fields, "__all__")

    def test_preparation_procedures_serializer(self):
        self.assertEqual(serializers.PreparationProceduresSerializer.Meta.model, models.PreparationProcedures)
        self.assertEqual(serializers.PreparationProceduresSerializer.Meta.fields, "__all__")

    def test_preparation_steps_serializer(self):
        self.assertEqual(serializers.PreparationStepsSerializer.Meta.model, models.PreparationSteps)
        self.assertEqual(serializers.PreparationStepsSerializer.Meta.fields, "__all__")

    def test_related_datastreams_serializer(self):
        self.assertEqual(serializers.RelatedDatastreamsSerializer.Meta.model, models.RelatedDatastreams)
        self.assertEqual(serializers.RelatedDatastreamsSerializer.Meta.fields, "__all__")

    def test_related_features_serializer(self):
        self.assertEqual(serializers.RelatedFeaturesSerializer.Meta.model, models.RelatedFeatures)
        self.assertEqual(serializers.RelatedFeaturesSerializer.Meta.fields, "__all__")

    def test_related_observations_serializer(self):
        self.assertEqual(serializers.RelatedObservationsSerializer.Meta.model, models.RelatedObservations)
        self.assertEqual(serializers.RelatedObservationsSerializer.Meta.fields, "__all__")

    def test_related_things_serializer(self):
        self.assertEqual(serializers.RelatedThingsSerializer.Meta.model, models.RelatedThings)
        self.assertEqual(serializers.RelatedThingsSerializer.Meta.fields, "__all__")

    def test_relation_roles_serializer(self):
        self.assertEqual(serializers.RelationRolesSerializer.Meta.model, models.RelationRoles)
        self.assertEqual(serializers.RelationRolesSerializer.Meta.fields, "__all__")

    def test_sampler_sampling_procedure_serializer(self):
        self.assertEqual(serializers.SamplerSamplingProcedureSerializer.Meta.model, models.SamplerSamplingProcedure)
        self.assertEqual(serializers.SamplerSamplingProcedureSerializer.Meta.fields, "__all__")

    def test_samplers_serializer(self):
        self.assertEqual(serializers.SamplersSerializer.Meta.model, models.Samplers)
        self.assertEqual(serializers.SamplersSerializer.Meta.fields, "__all__")

    def test_sampling_procedures_serializer(self):
        self.assertEqual(serializers.SamplingProceduresSerializer.Meta.model, models.SamplingProcedures)
        self.assertEqual(serializers.SamplingProceduresSerializer.Meta.fields, "__all__")

    def test_samplings_serializer(self):
        self.assertEqual(serializers.SamplingsSerializer.Meta.model, models.Samplings)
        self.assertEqual(serializers.SamplingsSerializer.Meta.fields, "__all__")

    def test_secondary_unit_lookup_serializer(self):
        self.assertEqual(serializers.SecondaryUnitLookupSerializer.Meta.model, models.SecondaryUnitLookup)
        self.assertEqual(serializers.SecondaryUnitLookupSerializer.Meta.fields, "__all__")

    def test_sensors_serializer(self):
        self.assertEqual(serializers.SensorsSerializer.Meta.model, models.Sensors)
        self.assertEqual(serializers.SensorsSerializer.Meta.fields, "__all__")

    def test_state_serializer(self):
        self.assertEqual(serializers.StateSerializer.Meta.model, models.State)
        self.assertEqual(serializers.StateSerializer.Meta.fields, "__all__")

    def test_state_lookup_serializer(self):
        self.assertEqual(serializers.StateLookupSerializer.Meta.model, models.StateLookup)
        self.assertEqual(serializers.StateLookupSerializer.Meta.fields, "__all__")

    def test_street_type_lookup_serializer(self):
        self.assertEqual(serializers.StreetTypeLookupSerializer.Meta.model, models.StreetTypeLookup)
        self.assertEqual(serializers.StreetTypeLookupSerializer.Meta.fields, "__all__")

    def test_tabblock_serializer(self):
        self.assertEqual(serializers.TabblockSerializer.Meta.model, models.Tabblock)
        self.assertEqual(serializers.TabblockSerializer.Meta.fields, "__all__")

    def test_tabblock20_serializer(self):
        self.assertEqual(serializers.Tabblock20Serializer.Meta.model, models.Tabblock20)
        self.assertEqual(serializers.Tabblock20Serializer.Meta.fields, "__all__")

    def test_things_serializer(self):
        self.assertEqual(serializers.ThingsSerializer.Meta.model, models.Things)
        self.assertEqual(serializers.ThingsSerializer.Meta.fields, "__all__")

    def test_things_locations_serializer(self):
        self.assertEqual(serializers.ThingsLocationsSerializer.Meta.model, models.ThingsLocations)
        self.assertEqual(serializers.ThingsLocationsSerializer.Meta.fields, "__all__")

    def test_topology_serializer(self):
        self.assertEqual(serializers.TopologySerializer.Meta.model, models.Topology)
        self.assertEqual(serializers.TopologySerializer.Meta.fields, "__all__")

    def test_tract_serializer(self):
        self.assertEqual(serializers.TractSerializer.Meta.model, models.Tract)
        self.assertEqual(serializers.TractSerializer.Meta.fields, "__all__")

    def test_zcta5_serializer(self):
        self.assertEqual(serializers.Zcta5Serializer.Meta.model, models.Zcta5)
        self.assertEqual(serializers.Zcta5Serializer.Meta.fields, "__all__")

    def test_zip_lookup_serializer(self):
        self.assertEqual(serializers.ZipLookupSerializer.Meta.model, models.ZipLookup)
        self.assertEqual(serializers.ZipLookupSerializer.Meta.fields, "__all__")

    def test_zip_lookup_all_serializer(self):
        self.assertEqual(serializers.ZipLookupAllSerializer.Meta.model, models.ZipLookupAll)
        self.assertEqual(serializers.ZipLookupAllSerializer.Meta.fields, "__all__")

    def test_zip_lookup_base_serializer(self):
        self.assertEqual(serializers.ZipLookupBaseSerializer.Meta.model, models.ZipLookupBase)
        self.assertEqual(serializers.ZipLookupBaseSerializer.Meta.fields, "__all__")

    def test_zip_state_serializer(self):
        self.assertEqual(serializers.ZipStateSerializer.Meta.model, models.ZipState)
        self.assertEqual(serializers.ZipStateSerializer.Meta.fields, "__all__")

    def test_zip_state_loc_serializer(self):
        self.assertEqual(serializers.ZipStateLocSerializer.Meta.model, models.ZipStateLoc)
        self.assertEqual(serializers.ZipStateLocSerializer.Meta.fields, "__all__")
