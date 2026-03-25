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
    pass

class Addrfeat(MetaModel, core.Addrfeat):
    pass

class Bg(MetaModel, core.Bg):
    pass

class County(MetaModel, core.County):
    pass

class CountyLookup(core.CountyLookup):
    pass

class CountysubLookup(core.CountysubLookup):
    pass

class Cousub(MetaModel, core.Cousub):
    pass

class Databasechangelog(MetaModel, core.Databasechangelog):
    pass

class Databasechangeloglock(MetaModel, core.Databasechangeloglock):
    pass

class Datastreams(MetaModel, core.Datastreams):
    pass

class DatastreamsFeaturesUltimate(core.DatastreamsFeaturesUltimate):
    pass

class DatastreamsObservedProperties(core.DatastreamsObservedProperties):
    pass

class DirectionLookup(MetaModel, core.DirectionLookup):
    pass

class Edges(MetaModel, core.Edges):
    pass

class Faces(MetaModel, core.Faces):
    pass

class Featnames(MetaModel, core.Featnames):
    pass

class FeatureTypes(MetaModel, core.FeatureTypes):
    pass

class Features(MetaModel, core.Features):
    pass

class FeaturesFeatureTypes(core.FeaturesFeatureTypes):
    pass

class GeocodeSettings(MetaModel, core.GeocodeSettings):
    pass

class GeocodeSettingsDefault(MetaModel, core.GeocodeSettingsDefault):
    pass

class HistLocations(MetaModel, core.HistLocations):
    pass

class Layer(core.Layer):
    pass

class LoaderLookuptables(MetaModel, core.LoaderLookuptables):
    pass

class LoaderPlatform(MetaModel, core.LoaderPlatform):
    pass

class LoaderVariables(MetaModel, core.LoaderVariables):
    pass

class Locations(MetaModel, core.Locations):
    pass

class LocationsHistLocations(core.LocationsHistLocations):
    pass

class Observations(MetaModel, core.Observations):
    pass

class ObservedProperties(MetaModel, core.ObservedProperties):
    pass

class PagcGaz(MetaModel, core.PagcGaz):
    pass

class PagcLex(MetaModel, core.PagcLex):
    pass

class PagcRules(MetaModel, core.PagcRules):
    pass

class Place(MetaModel, core.Place):
    pass

class PlaceLookup(core.PlaceLookup):
    pass

class PreparationProcedures(MetaModel, core.PreparationProcedures):
    pass

class PreparationSteps(MetaModel, core.PreparationSteps):
    pass

class RelatedDatastreams(MetaModel, core.RelatedDatastreams):
    pass

class RelatedFeatures(MetaModel, core.RelatedFeatures):
    pass

class RelatedObservations(MetaModel, core.RelatedObservations):
    pass

class RelatedThings(MetaModel, core.RelatedThings):
    pass

class RelationRoles(MetaModel, core.RelationRoles):
    pass

class SamplerSamplingProcedure(core.SamplerSamplingProcedure):
    pass

class Samplers(MetaModel, core.Samplers):
    pass

class SamplingProcedures(MetaModel, core.SamplingProcedures):
    pass

class Samplings(MetaModel, core.Samplings):
    pass

class SecondaryUnitLookup(MetaModel, core.SecondaryUnitLookup):
    pass

class Sensors(MetaModel, core.Sensors):
    pass

class State(MetaModel, core.State):
    pass

class StateLookup(MetaModel, core.StateLookup):
    pass

class StreetTypeLookup(MetaModel, core.StreetTypeLookup):
    pass

class Tabblock(MetaModel, core.Tabblock):
    pass

class Tabblock20(MetaModel, core.Tabblock20):
    pass

class Things(MetaModel, core.Things):
    pass

class ThingsLocations(core.ThingsLocations):
    pass

class Topology(MetaModel, core.Topology):
    pass

class Tract(MetaModel, core.Tract):
    pass

class Zcta5(core.Zcta5):
    pass

class ZipLookup(MetaModel, core.ZipLookup):
    pass

class ZipLookupAll(MetaModel, core.ZipLookupAll):
    pass

class ZipLookupBase(MetaModel, core.ZipLookupBase):
    pass

class ZipState(core.ZipState):
    pass

class ZipStateLoc(core.ZipStateLoc):
    pass
