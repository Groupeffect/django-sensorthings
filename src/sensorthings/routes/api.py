from rest_framework import routers
from sensorthings import views

router = routers.DefaultRouter()

router.register(r"Addr", views.AddrViewset, basename="addr")
router.register(r"Addrfeat", views.AddrfeatViewset, basename="addrfeat")
router.register(r"Bg", views.BgViewset, basename="bg")
router.register(r"County", views.CountyViewset, basename="county")
router.register(r"CountyLookup", views.CountyLookupViewset, basename="countylookup")
router.register(
    r"CountysubLookup", views.CountysubLookupViewset, basename="countysublookup"
)
router.register(r"Cousub", views.CousubViewset, basename="cousub")
router.register(
    r"Databasechangelog", views.DatabasechangelogViewset, basename="databasechangelog"
)
router.register(
    r"Databasechangeloglock",
    views.DatabasechangeloglockViewset,
    basename="databasechangeloglock",
)
router.register(r"Datastreams", views.DatastreamsViewset, basename="datastreams")
router.register(
    r"DatastreamsFeaturesUltimate",
    views.DatastreamsFeaturesUltimateViewset,
    basename="datastreamsfeaturesultimate",
)
router.register(
    r"DatastreamsObservedProperties",
    views.DatastreamsObservedPropertiesViewset,
    basename="datastreamsobservedproperties",
)
router.register(
    r"DirectionLookup", views.DirectionLookupViewset, basename="directionlookup"
)
router.register(r"Edges", views.EdgesViewset, basename="edges")
router.register(r"Faces", views.FacesViewset, basename="faces")
router.register(r"Featnames", views.FeatnamesViewset, basename="featnames")
router.register(r"FeatureTypes", views.FeatureTypesViewset, basename="featuretypes")
router.register(r"Features", views.FeaturesViewset, basename="features")
router.register(
    r"FeaturesFeatureTypes",
    views.FeaturesFeatureTypesViewset,
    basename="featuresfeaturetypes",
)
router.register(
    r"GeocodeSettings", views.GeocodeSettingsViewset, basename="geocodesettings"
)
router.register(
    r"GeocodeSettingsDefault",
    views.GeocodeSettingsDefaultViewset,
    basename="geocodesettingsdefault",
)
router.register(r"HistLocations", views.HistLocationsViewset, basename="histlocations")
router.register(r"Layer", views.LayerViewset, basename="layer")
router.register(
    r"LoaderLookuptables",
    views.LoaderLookuptablesViewset,
    basename="loaderlookuptables",
)
router.register(
    r"LoaderPlatform", views.LoaderPlatformViewset, basename="loaderplatform"
)
router.register(
    r"LoaderVariables", views.LoaderVariablesViewset, basename="loadervariables"
)
router.register(r"Locations", views.LocationsViewset, basename="locations")
router.register(
    r"LocationsHistLocations",
    views.LocationsHistLocationsViewset,
    basename="locationshistlocations",
)
router.register(r"Observations", views.ObservationsViewset, basename="observations")
router.register(
    r"ObservedProperties",
    views.ObservedPropertiesViewset,
    basename="observedproperties",
)
router.register(r"PagcGaz", views.PagcGazViewset, basename="pagcgaz")
router.register(r"PagcLex", views.PagcLexViewset, basename="pagclex")
router.register(r"PagcRules", views.PagcRulesViewset, basename="pagcrules")
router.register(r"Place", views.PlaceViewset, basename="place")
router.register(r"PlaceLookup", views.PlaceLookupViewset, basename="placelookup")
router.register(
    r"PreparationProcedures",
    views.PreparationProceduresViewset,
    basename="preparationprocedures",
)
router.register(
    r"PreparationSteps", views.PreparationStepsViewset, basename="preparationsteps"
)
router.register(
    r"RelatedDatastreams",
    views.RelatedDatastreamsViewset,
    basename="relateddatastreams",
)
router.register(
    r"RelatedFeatures", views.RelatedFeaturesViewset, basename="relatedfeatures"
)
router.register(
    r"RelatedObservations",
    views.RelatedObservationsViewset,
    basename="relatedobservations",
)
router.register(r"RelatedThings", views.RelatedThingsViewset, basename="relatedthings")
router.register(r"RelationRoles", views.RelationRolesViewset, basename="relationroles")
router.register(
    r"SamplerSamplingProcedure",
    views.SamplerSamplingProcedureViewset,
    basename="samplersamplingprocedure",
)
router.register(r"Samplers", views.SamplersViewset, basename="samplers")
router.register(
    r"SamplingProcedures",
    views.SamplingProceduresViewset,
    basename="samplingprocedures",
)
router.register(r"Samplings", views.SamplingsViewset, basename="samplings")
router.register(
    r"SecondaryUnitLookup",
    views.SecondaryUnitLookupViewset,
    basename="secondaryunitlookup",
)
router.register(r"Sensors", views.SensorsViewset, basename="sensors")
router.register(r"State", views.StateViewset, basename="state")
router.register(r"StateLookup", views.StateLookupViewset, basename="statelookup")
router.register(
    r"StreetTypeLookup", views.StreetTypeLookupViewset, basename="streettypelookup"
)
router.register(r"Tabblock", views.TabblockViewset, basename="tabblock")
router.register(r"Tabblock20", views.Tabblock20Viewset, basename="tabblock20")
router.register(r"Things", views.ThingsViewset, basename="things")
router.register(
    r"ThingsLocations", views.ThingsLocationsViewset, basename="thingslocations"
)
router.register(r"Topology", views.TopologyViewset, basename="topology")
router.register(r"Tract", views.TractViewset, basename="tract")
router.register(r"Zcta5", views.Zcta5Viewset, basename="zcta5")
router.register(r"ZipLookup", views.ZipLookupViewset, basename="ziplookup")
router.register(r"ZipLookupAll", views.ZipLookupAllViewset, basename="ziplookupall")
router.register(r"ZipLookupBase", views.ZipLookupBaseViewset, basename="ziplookupbase")
router.register(r"ZipState", views.ZipStateViewset, basename="zipstate")
router.register(r"ZipStateLoc", views.ZipStateLocViewset, basename="zipstateloc")

urlpatterns = router.urls
