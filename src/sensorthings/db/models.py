from sensorthings.db import core
from django.contrib.gis.db import models
from django.conf import settings

bn = {"blank": True, "null": True}

class MetaModel(models.Model):
    if not hasattr(settings, "SENSORTHINGS_ENABLE_PUBLIC_PRIVATE") or settings.SENSORTHINGS_ENABLE_PUBLIC_PRIVATE is True:
        is_public = models.BooleanField(default=True)
        is_private = models.BooleanField(default=False)

    if not hasattr(settings, "SENSORTHINGS_ENABLE_OWNER") or settings.SENSORTHINGS_ENABLE_OWNER is True:
        has_owner = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **bn, related_name="%(class)s_owner"
        )
        has_members = models.ManyToManyField(
            settings.AUTH_USER_MODEL, blank=True, related_name="%(class)s_members"
        )

    class Meta:
        abstract = True

class Addr(MetaModel, core.Addr):
    class Meta:
        db_table = "addr"

class Addrfeat(MetaModel, core.Addrfeat):
    class Meta:
        db_table = "addrfeat"

class Bg(MetaModel, core.Bg):
    class Meta:
        db_table = "bg"

class County(MetaModel, core.County):
    class Meta:
        db_table = "county"

class CountyLookup(core.CountyLookup):
    class Meta:
        db_table = "county_lookup"

class CountysubLookup(core.CountysubLookup):
    class Meta:
        db_table = "countysub_lookup"

class Cousub(MetaModel, core.Cousub):
    class Meta:
        db_table = "cousub"

class Databasechangelog(MetaModel, core.Databasechangelog):
    class Meta:
        db_table = "databasechangelog"

class Databasechangeloglock(MetaModel, core.Databasechangeloglock):
    class Meta:
        db_table = "databasechangeloglock"

class Datastreams(MetaModel, core.Datastreams):
    class Meta:
        db_table = "datastreams"

class DatastreamsFeaturesUltimate(core.DatastreamsFeaturesUltimate):
    class Meta:
        db_table = "datastreams_features_ultimate"

class DatastreamsObservedProperties(core.DatastreamsObservedProperties):
    class Meta:
        db_table = "datastreams_observed_properties"

class DirectionLookup(MetaModel, core.DirectionLookup):
    class Meta:
        db_table = "direction_lookup"

class Edges(MetaModel, core.Edges):
    class Meta:
        db_table = "edges"

class Faces(MetaModel, core.Faces):
    class Meta:
        db_table = "faces"

class Featnames(MetaModel, core.Featnames):
    class Meta:
        db_table = "featnames"

class FeatureTypes(MetaModel, core.FeatureTypes):
    class Meta:
        db_table = "feature_types"

class Features(MetaModel, core.Features):
    class Meta:
        db_table = "features"

class FeaturesFeatureTypes(core.FeaturesFeatureTypes):
    class Meta:
        db_table = "features_feature_types"

class GeocodeSettings(MetaModel, core.GeocodeSettings):
    class Meta:
        db_table = "geocode_settings"

class GeocodeSettingsDefault(MetaModel, core.GeocodeSettingsDefault):
    class Meta:
        db_table = "geocode_settings_default"

class HistLocations(MetaModel, core.HistLocations):
    class Meta:
        db_table = "hist_locations"

class Layer(core.Layer):
    class Meta:
        db_table = "layer"

class LoaderLookuptables(MetaModel, core.LoaderLookuptables):
    class Meta:
        db_table = "loader_lookuptables"

class LoaderPlatform(MetaModel, core.LoaderPlatform):
    class Meta:
        db_table = "loader_platform"

class LoaderVariables(MetaModel, core.LoaderVariables):
    class Meta:
        db_table = "loader_variables"

class Locations(MetaModel, core.Locations):
    class Meta:
        db_table = "locations"

class LocationsHistLocations(core.LocationsHistLocations):
    class Meta:
        db_table = "locations_hist_locations"

class Observations(MetaModel, core.Observations):
    class Meta:
        db_table = "observations"

class ObservedProperties(MetaModel, core.ObservedProperties):
    class Meta:
        db_table = "observed_properties"

class PagcGaz(MetaModel, core.PagcGaz):
    class Meta:
        db_table = "pagc_gaz"

class PagcLex(MetaModel, core.PagcLex):
    class Meta:
        db_table = "pagc_lex"

class PagcRules(MetaModel, core.PagcRules):
    class Meta:
        db_table = "pagc_rules"

class Place(MetaModel, core.Place):
    class Meta:
        db_table = "place"

class PlaceLookup(core.PlaceLookup):
    class Meta:
        db_table = "place_lookup"

class PreparationProcedures(MetaModel, core.PreparationProcedures):
    class Meta:
        db_table = "preparation_procedures"

class PreparationSteps(MetaModel, core.PreparationSteps):
    class Meta:
        db_table = "preparation_steps"

class RelatedDatastreams(MetaModel, core.RelatedDatastreams):
    class Meta:
        db_table = "related_datastreams"

class RelatedFeatures(MetaModel, core.RelatedFeatures):
    class Meta:
        db_table = "related_features"

class RelatedObservations(MetaModel, core.RelatedObservations):
    class Meta:
        db_table = "related_observations"

class RelatedThings(MetaModel, core.RelatedThings):
    class Meta:
        db_table = "related_things"

class RelationRoles(MetaModel, core.RelationRoles):
    class Meta:
        db_table = "relation_roles"

class SamplerSamplingProcedure(core.SamplerSamplingProcedure):
    class Meta:
        db_table = "sampler_sampling_procedure"

class Samplers(MetaModel, core.Samplers):
    class Meta:
        db_table = "samplers"

class SamplingProcedures(MetaModel, core.SamplingProcedures):
    class Meta:
        db_table = "sampling_procedures"

class Samplings(MetaModel, core.Samplings):
    class Meta:
        db_table = "samplings"

class SecondaryUnitLookup(MetaModel, core.SecondaryUnitLookup):
    class Meta:
        db_table = "secondary_unit_lookup"

class Sensors(MetaModel, core.Sensors):
    class Meta:
        db_table = "sensors"

class State(MetaModel, core.State):
    class Meta:
        db_table = "state"

class StateLookup(MetaModel, core.StateLookup):
    class Meta:
        db_table = "state_lookup"

class StreetTypeLookup(MetaModel, core.StreetTypeLookup):
    class Meta:
        db_table = "street_type_lookup"

class Tabblock(MetaModel, core.Tabblock):
    class Meta:
        db_table = "tabblock"

class Tabblock20(MetaModel, core.Tabblock20):
    class Meta:
        db_table = "tabblock20"

class Things(MetaModel, core.Things):
    class Meta:
        db_table = "things"

class ThingsLocations(core.ThingsLocations):
    class Meta:
        db_table = "things_locations"

class Topology(MetaModel, core.Topology):
    class Meta:
        db_table = "topology"

class Tract(MetaModel, core.Tract):
    class Meta:
        db_table = "tract"

class Zcta5(core.Zcta5):
    class Meta:
        db_table = "zcta5"

class ZipLookup(MetaModel, core.ZipLookup):
    class Meta:
        db_table = "zip_lookup"

class ZipLookupAll(MetaModel, core.ZipLookupAll):
    class Meta:
        db_table = "zip_lookup_all"

class ZipLookupBase(MetaModel, core.ZipLookupBase):
    class Meta:
        db_table = "zip_lookup_base"

class ZipState(core.ZipState):
    class Meta:
        db_table = "zip_state"

class ZipStateLoc(core.ZipStateLoc):
    class Meta:
        db_table = "zip_state_loc"
