from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from sensorthings import serializers
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.conf import settings


def set_filterset_fields_exclude(serializer_class):
    fields = [
        "JSONField",
        "PointField",
        "MultiPointField",
        "PolygonField",
        "MultiPolygonField",
        "LineStringField",
        "MultiLineStringField",
        "GenericForeignKey",
        "FileField",
        "CompositePrimaryKey",
        "GeometryField",
        "ForeignKey",
        "OneToOneField",
        "ManyToManyField",
        "ManyToManyRel",
        "ManyToOneRel",
    ]
    result = []
    for field in serializer_class.Meta.model._meta.get_fields():
        if field.__class__.__name__ not in fields:
            result.append(field.name)

    return result


class MetaViewset(ModelViewSet):
    serializer_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    def get_queryset(self):
        if (
            settings.SENSORTHINGS_ENABLE_PUBLIC_PRIVATE
            and settings.SENSORTHINGS_ENABLE_OWNER
        ):
            return self.serializer_class.Meta.model.objects.filter(
                Q(has_owner=self.request.user) | Q(is_public=True)
            ).exclude(is_private=True)
        elif settings.SENSORTHINGS_ENABLE_PUBLIC_PRIVATE:
            return self.serializer_class.Meta.model.objects.filter(
                is_public=True
            ).exclude(is_private=True)

        elif settings.SENSORTHINGS_ENABLE_OWNER:
            return self.serializer_class.Meta.model.objects.filter(
                has_owner=self.request.user
            )
        else:
            return self.serializer_class.Meta.model.objects.all()


class AddrViewset(MetaViewset):
    serializer_class = serializers.AddrSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class AddrfeatViewset(MetaViewset):
    serializer_class = serializers.AddrfeatSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class BgViewset(MetaViewset):
    serializer_class = serializers.BgSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class CountyViewset(MetaViewset):
    serializer_class = serializers.CountySerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class CountyLookupViewset(MetaViewset):
    serializer_class = serializers.CountyLookupSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class CountysubLookupViewset(MetaViewset):
    serializer_class = serializers.CountysubLookupSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class CousubViewset(MetaViewset):
    serializer_class = serializers.CousubSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class DatabasechangelogViewset(MetaViewset):
    serializer_class = serializers.DatabasechangelogSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class DatabasechangeloglockViewset(MetaViewset):
    serializer_class = serializers.DatabasechangeloglockSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class DatastreamsViewset(MetaViewset):
    serializer_class = serializers.DatastreamsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class DatastreamsFeaturesUltimateViewset(MetaViewset):
    serializer_class = serializers.DatastreamsFeaturesUltimateSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class DatastreamsObservedPropertiesViewset(MetaViewset):
    serializer_class = serializers.DatastreamsObservedPropertiesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class DirectionLookupViewset(MetaViewset):
    serializer_class = serializers.DirectionLookupSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class EdgesViewset(MetaViewset):
    serializer_class = serializers.EdgesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class FacesViewset(MetaViewset):
    serializer_class = serializers.FacesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class FeatnamesViewset(MetaViewset):
    serializer_class = serializers.FeatnamesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class FeatureTypesViewset(MetaViewset):
    serializer_class = serializers.FeatureTypesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class FeaturesViewset(MetaViewset):
    serializer_class = serializers.FeaturesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class FeaturesFeatureTypesViewset(MetaViewset):
    serializer_class = serializers.FeaturesFeatureTypesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class GeocodeSettingsViewset(MetaViewset):
    serializer_class = serializers.GeocodeSettingsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class GeocodeSettingsDefaultViewset(MetaViewset):
    serializer_class = serializers.GeocodeSettingsDefaultSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class HistLocationsViewset(MetaViewset):
    serializer_class = serializers.HistLocationsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class LayerViewset(MetaViewset):
    serializer_class = serializers.LayerSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class LoaderLookuptablesViewset(MetaViewset):
    serializer_class = serializers.LoaderLookuptablesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class LoaderPlatformViewset(MetaViewset):
    serializer_class = serializers.LoaderPlatformSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class LoaderVariablesViewset(MetaViewset):
    serializer_class = serializers.LoaderVariablesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class LocationsViewset(MetaViewset):
    serializer_class = serializers.LocationsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class LocationsHistLocationsViewset(MetaViewset):
    serializer_class = serializers.LocationsHistLocationsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class ObservationsViewset(MetaViewset):
    serializer_class = serializers.ObservationsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class ObservedPropertiesViewset(MetaViewset):
    serializer_class = serializers.ObservedPropertiesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class PagcGazViewset(MetaViewset):
    serializer_class = serializers.PagcGazSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class PagcLexViewset(MetaViewset):
    serializer_class = serializers.PagcLexSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class PagcRulesViewset(MetaViewset):
    serializer_class = serializers.PagcRulesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class PlaceViewset(MetaViewset):
    serializer_class = serializers.PlaceSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class PlaceLookupViewset(MetaViewset):
    serializer_class = serializers.PlaceLookupSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class PreparationProceduresViewset(MetaViewset):
    serializer_class = serializers.PreparationProceduresSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class PreparationStepsViewset(MetaViewset):
    serializer_class = serializers.PreparationStepsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class RelatedDatastreamsViewset(MetaViewset):
    serializer_class = serializers.RelatedDatastreamsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class RelatedFeaturesViewset(MetaViewset):
    serializer_class = serializers.RelatedFeaturesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class RelatedObservationsViewset(MetaViewset):
    serializer_class = serializers.RelatedObservationsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class RelatedThingsViewset(MetaViewset):
    serializer_class = serializers.RelatedThingsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class RelationRolesViewset(MetaViewset):
    serializer_class = serializers.RelationRolesSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class SamplerSamplingProcedureViewset(MetaViewset):
    serializer_class = serializers.SamplerSamplingProcedureSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class SamplersViewset(MetaViewset):
    serializer_class = serializers.SamplersSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class SamplingProceduresViewset(MetaViewset):
    serializer_class = serializers.SamplingProceduresSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class SamplingsViewset(MetaViewset):
    serializer_class = serializers.SamplingsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class SecondaryUnitLookupViewset(MetaViewset):
    serializer_class = serializers.SecondaryUnitLookupSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class SensorsViewset(MetaViewset):
    serializer_class = serializers.SensorsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class StateViewset(MetaViewset):
    serializer_class = serializers.StateSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class StateLookupViewset(MetaViewset):
    serializer_class = serializers.StateLookupSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class StreetTypeLookupViewset(MetaViewset):
    serializer_class = serializers.StreetTypeLookupSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class TabblockViewset(MetaViewset):
    serializer_class = serializers.TabblockSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class Tabblock20Viewset(MetaViewset):
    serializer_class = serializers.Tabblock20Serializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class ThingsViewset(MetaViewset):
    serializer_class = serializers.ThingsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class ThingsLocationsViewset(MetaViewset):
    serializer_class = serializers.ThingsLocationsSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class TopologyViewset(MetaViewset):
    serializer_class = serializers.TopologySerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class TractViewset(MetaViewset):
    serializer_class = serializers.TractSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class Zcta5Viewset(MetaViewset):
    serializer_class = serializers.Zcta5Serializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class ZipLookupViewset(MetaViewset):
    serializer_class = serializers.ZipLookupSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class ZipLookupAllViewset(MetaViewset):
    serializer_class = serializers.ZipLookupAllSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class ZipLookupBaseViewset(MetaViewset):
    serializer_class = serializers.ZipLookupBaseSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class ZipStateViewset(MetaViewset):
    serializer_class = serializers.ZipStateSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]


class ZipStateLocViewset(MetaViewset):
    serializer_class = serializers.ZipStateLocSerializer
    filterset_fields = set_filterset_fields_exclude(serializer_class)
    search_fields = filterset_fields + ["id"]
