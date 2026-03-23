from rest_framework import serializers
from sensorthings import models


class MetaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = None


class AddrSerializer(MetaModelSerializer):
    class Meta:
        model = models.Addr
        fields = "__all__"


class AddrfeatSerializer(MetaModelSerializer):
    class Meta:
        model = models.Addrfeat
        fields = "__all__"


class BgSerializer(MetaModelSerializer):
    class Meta:
        model = models.Bg
        fields = "__all__"


class CountySerializer(MetaModelSerializer):
    class Meta:
        model = models.County
        fields = "__all__"


class CountyLookupSerializer(MetaModelSerializer):
    class Meta:
        model = models.CountyLookup
        fields = "__all__"


class CountysubLookupSerializer(MetaModelSerializer):
    class Meta:
        model = models.CountysubLookup
        fields = "__all__"


class CousubSerializer(MetaModelSerializer):
    class Meta:
        model = models.Cousub
        fields = "__all__"


class DatabasechangelogSerializer(MetaModelSerializer):
    class Meta:
        model = models.Databasechangelog
        fields = "__all__"


class DatabasechangeloglockSerializer(MetaModelSerializer):
    class Meta:
        model = models.Databasechangeloglock
        fields = "__all__"


class DatastreamsSerializer(MetaModelSerializer):
    class Meta:
        model = models.Datastreams
        fields = "__all__"


class DatastreamsFeaturesUltimateSerializer(MetaModelSerializer):
    class Meta:
        model = models.DatastreamsFeaturesUltimate
        fields = "__all__"


class DatastreamsObservedPropertiesSerializer(MetaModelSerializer):
    class Meta:
        model = models.DatastreamsObservedProperties
        fields = "__all__"


class DirectionLookupSerializer(MetaModelSerializer):
    class Meta:
        model = models.DirectionLookup
        fields = "__all__"


class EdgesSerializer(MetaModelSerializer):
    class Meta:
        model = models.Edges
        fields = "__all__"


class FacesSerializer(MetaModelSerializer):
    class Meta:
        model = models.Faces
        fields = "__all__"


class FeatnamesSerializer(MetaModelSerializer):
    class Meta:
        model = models.Featnames
        fields = "__all__"


class FeatureTypesSerializer(MetaModelSerializer):
    class Meta:
        model = models.FeatureTypes
        fields = "__all__"


class FeaturesSerializer(MetaModelSerializer):
    class Meta:
        model = models.Features
        fields = "__all__"


class FeaturesFeatureTypesSerializer(MetaModelSerializer):
    class Meta:
        model = models.FeaturesFeatureTypes
        fields = "__all__"


class GeocodeSettingsSerializer(MetaModelSerializer):
    class Meta:
        model = models.GeocodeSettings
        fields = "__all__"


class GeocodeSettingsDefaultSerializer(MetaModelSerializer):
    class Meta:
        model = models.GeocodeSettingsDefault
        fields = "__all__"


class HistLocationsSerializer(MetaModelSerializer):
    class Meta:
        model = models.HistLocations
        fields = "__all__"


class LayerSerializer(MetaModelSerializer):
    class Meta:
        model = models.Layer
        fields = "__all__"


class LoaderLookuptablesSerializer(MetaModelSerializer):
    class Meta:
        model = models.LoaderLookuptables
        fields = "__all__"


class LoaderPlatformSerializer(MetaModelSerializer):
    class Meta:
        model = models.LoaderPlatform
        fields = "__all__"


class LoaderVariablesSerializer(MetaModelSerializer):
    class Meta:
        model = models.LoaderVariables
        fields = "__all__"


class LocationsSerializer(MetaModelSerializer):
    class Meta:
        model = models.Locations
        fields = "__all__"


class LocationsHistLocationsSerializer(MetaModelSerializer):
    class Meta:
        model = models.LocationsHistLocations
        fields = "__all__"


class ObservationsSerializer(MetaModelSerializer):
    class Meta:
        model = models.Observations
        fields = "__all__"


class ObservedPropertiesSerializer(MetaModelSerializer):
    class Meta:
        model = models.ObservedProperties
        fields = "__all__"


class PagcGazSerializer(MetaModelSerializer):
    class Meta:
        model = models.PagcGaz
        fields = "__all__"


class PagcLexSerializer(MetaModelSerializer):
    class Meta:
        model = models.PagcLex
        fields = "__all__"


class PagcRulesSerializer(MetaModelSerializer):
    class Meta:
        model = models.PagcRules
        fields = "__all__"


class PlaceSerializer(MetaModelSerializer):
    class Meta:
        model = models.Place
        fields = "__all__"


class PlaceLookupSerializer(MetaModelSerializer):
    class Meta:
        model = models.PlaceLookup
        fields = "__all__"


class PreparationProceduresSerializer(MetaModelSerializer):
    class Meta:
        model = models.PreparationProcedures
        fields = "__all__"


class PreparationStepsSerializer(MetaModelSerializer):
    class Meta:
        model = models.PreparationSteps
        fields = "__all__"


class RelatedDatastreamsSerializer(MetaModelSerializer):
    class Meta:
        model = models.RelatedDatastreams
        fields = "__all__"


class RelatedFeaturesSerializer(MetaModelSerializer):
    class Meta:
        model = models.RelatedFeatures
        fields = "__all__"


class RelatedObservationsSerializer(MetaModelSerializer):
    class Meta:
        model = models.RelatedObservations
        fields = "__all__"


class RelatedThingsSerializer(MetaModelSerializer):
    class Meta:
        model = models.RelatedThings
        fields = "__all__"


class RelationRolesSerializer(MetaModelSerializer):
    class Meta:
        model = models.RelationRoles
        fields = "__all__"


class SamplerSamplingProcedureSerializer(MetaModelSerializer):
    class Meta:
        model = models.SamplerSamplingProcedure
        fields = "__all__"


class SamplersSerializer(MetaModelSerializer):
    class Meta:
        model = models.Samplers
        fields = "__all__"


class SamplingProceduresSerializer(MetaModelSerializer):
    class Meta:
        model = models.SamplingProcedures
        fields = "__all__"


class SamplingsSerializer(MetaModelSerializer):
    class Meta:
        model = models.Samplings
        fields = "__all__"


class SecondaryUnitLookupSerializer(MetaModelSerializer):
    class Meta:
        model = models.SecondaryUnitLookup
        fields = "__all__"


class SensorsSerializer(MetaModelSerializer):
    class Meta:
        model = models.Sensors
        fields = "__all__"


class StateSerializer(MetaModelSerializer):
    class Meta:
        model = models.State
        fields = "__all__"


class StateLookupSerializer(MetaModelSerializer):
    class Meta:
        model = models.StateLookup
        fields = "__all__"


class StreetTypeLookupSerializer(MetaModelSerializer):
    class Meta:
        model = models.StreetTypeLookup
        fields = "__all__"


class TabblockSerializer(MetaModelSerializer):
    class Meta:
        model = models.Tabblock
        fields = "__all__"


class Tabblock20Serializer(MetaModelSerializer):
    class Meta:
        model = models.Tabblock20
        fields = "__all__"


class ThingsSerializer(MetaModelSerializer):
    class Meta:
        model = models.Things
        fields = "__all__"


class ThingsLocationsSerializer(MetaModelSerializer):
    class Meta:
        model = models.ThingsLocations
        fields = "__all__"


class TopologySerializer(MetaModelSerializer):
    class Meta:
        model = models.Topology
        fields = "__all__"


class TractSerializer(MetaModelSerializer):
    class Meta:
        model = models.Tract
        fields = "__all__"


class Zcta5Serializer(MetaModelSerializer):
    class Meta:
        model = models.Zcta5
        fields = "__all__"


class ZipLookupSerializer(MetaModelSerializer):
    class Meta:
        model = models.ZipLookup
        fields = "__all__"


class ZipLookupAllSerializer(MetaModelSerializer):
    class Meta:
        model = models.ZipLookupAll
        fields = "__all__"


class ZipLookupBaseSerializer(MetaModelSerializer):
    class Meta:
        model = models.ZipLookupBase
        fields = "__all__"


class ZipStateSerializer(MetaModelSerializer):
    class Meta:
        model = models.ZipState
        fields = "__all__"


class ZipStateLocSerializer(MetaModelSerializer):
    class Meta:
        model = models.ZipStateLoc
        fields = "__all__"
