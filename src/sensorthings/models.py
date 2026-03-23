from django.contrib.gis.db import models
from django.conf import settings

bn = {"blank": True, "null": True}


class MetaModel(models.Model):
    if (
        not hasattr(settings, "SENSORTHINGS_ENABLE_PUBLIC_PRIVATE")
        or settings.SENSORTHINGS_ENABLE_PUBLIC_PRIVATE is not False
    ):
        is_public = models.BooleanField(default=True)
        is_private = models.BooleanField(default=False)
    if (
        not hasattr(settings, "SENSORTHINGS_ENABLE_OWNER")
        or settings.SENSORTHINGS_ENABLE_OWNER is not False
    ):
        has_owner = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **bn
        )

    class Meta:
        abstract = True


class Addr(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    tlid = models.BigIntegerField(**bn)
    fromhn = models.CharField(max_length=12, **bn)
    tohn = models.CharField(max_length=12, **bn)
    side = models.CharField(max_length=1, **bn)
    zip = models.CharField(max_length=5, **bn)
    plus4 = models.CharField(max_length=4, **bn)
    fromtyp = models.CharField(max_length=1, **bn)
    totyp = models.CharField(max_length=1, **bn)
    fromarmid = models.IntegerField(**bn)
    toarmid = models.IntegerField(**bn)
    arid = models.CharField(max_length=22, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    statefp = models.CharField(max_length=2, **bn)

    class Meta:

        db_table = "addr"
        verbose_name_plural = db_table


class Addrfeat(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    tlid = models.BigIntegerField(**bn)
    statefp = models.CharField(max_length=2)
    aridl = models.CharField(max_length=22, **bn)
    aridr = models.CharField(max_length=22, **bn)
    linearid = models.CharField(max_length=22, **bn)
    fullname = models.CharField(max_length=100, **bn)
    lfromhn = models.CharField(max_length=12, **bn)
    ltohn = models.CharField(max_length=12, **bn)
    rfromhn = models.CharField(max_length=12, **bn)
    rtohn = models.CharField(max_length=12, **bn)
    zipl = models.CharField(max_length=5, **bn)
    zipr = models.CharField(max_length=5, **bn)
    edge_mtfcc = models.CharField(max_length=5, **bn)
    parityl = models.CharField(max_length=1, **bn)
    parityr = models.CharField(max_length=1, **bn)
    plus4l = models.CharField(max_length=4, **bn)
    plus4r = models.CharField(max_length=4, **bn)
    lfromtyp = models.CharField(max_length=1, **bn)
    ltotyp = models.CharField(max_length=1, **bn)
    rfromtyp = models.CharField(max_length=1, **bn)
    rtotyp = models.CharField(max_length=1, **bn)
    offsetl = models.CharField(max_length=1, **bn)
    offsetr = models.CharField(max_length=1, **bn)
    the_geom = models.LineStringField(srid=4269, **bn)

    class Meta:

        db_table = "addrfeat"


class Bg(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    statefp = models.CharField(max_length=2, **bn)
    countyfp = models.CharField(max_length=3, **bn)
    tractce = models.CharField(max_length=6, **bn)
    blkgrpce = models.CharField(max_length=1, **bn)
    bg_id = models.CharField(**bn, max_length=12)
    namelsad = models.CharField(max_length=13, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    funcstat = models.CharField(max_length=1, **bn)
    aland = models.FloatField(**bn)
    awater = models.FloatField(**bn)
    intptlat = models.CharField(max_length=11, **bn)
    intptlon = models.CharField(max_length=12, **bn)
    the_geom = models.MultiPolygonField(srid=4269, **bn)

    class Meta:

        db_table = "bg"
        db_table_comment = "block groups"
        verbose_name_plural = db_table


class County(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    statefp = models.CharField(max_length=2, **bn)
    countyfp = models.CharField(max_length=3, **bn)
    countyns = models.CharField(max_length=8, **bn)
    cntyidfp = models.CharField(**bn, max_length=5)
    name = models.CharField(max_length=100, **bn)
    namelsad = models.CharField(max_length=100, **bn)
    lsad = models.CharField(max_length=2, **bn)
    classfp = models.CharField(max_length=2, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    csafp = models.CharField(max_length=3, **bn)
    cbsafp = models.CharField(max_length=5, **bn)
    metdivfp = models.CharField(max_length=5, **bn)
    funcstat = models.CharField(max_length=1, **bn)
    aland = models.BigIntegerField(**bn)
    awater = models.FloatField(**bn)
    intptlat = models.CharField(max_length=11, **bn)
    intptlon = models.CharField(max_length=12, **bn)
    the_geom = models.MultiPolygonField(srid=4269, **bn)

    class Meta:
        db_table = "county"
        verbose_name_plural = db_table


class CountyLookup(MetaModel):
    pk = models.CompositePrimaryKey("st_code", "co_code")
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, **bn)
    co_code = models.IntegerField()
    name = models.CharField(max_length=90, **bn)

    class Meta:

        db_table = "county_lookup"


class CountysubLookup(MetaModel):
    pk = models.CompositePrimaryKey("st_code", "co_code", "cs_code")
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, **bn)
    co_code = models.IntegerField()
    county = models.CharField(max_length=90, **bn)
    cs_code = models.IntegerField()
    name = models.CharField(max_length=90, **bn)

    class Meta:

        db_table = "countysub_lookup"


class Cousub(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    statefp = models.CharField(max_length=2, **bn)
    countyfp = models.CharField(max_length=3, **bn)
    cousubfp = models.CharField(max_length=5, **bn)
    cousubns = models.CharField(max_length=8, **bn)
    cosbidfp = models.CharField(**bn, max_length=10)
    name = models.CharField(max_length=100, **bn)
    namelsad = models.CharField(max_length=100, **bn)
    lsad = models.CharField(max_length=2, **bn)
    classfp = models.CharField(max_length=2, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    cnectafp = models.CharField(max_length=3, **bn)
    nectafp = models.CharField(max_length=5, **bn)
    nctadvfp = models.CharField(max_length=5, **bn)
    funcstat = models.CharField(max_length=1, **bn)
    aland = models.DecimalField(max_digits=14, decimal_places=0, **bn)
    awater = models.DecimalField(max_digits=14, decimal_places=0, **bn)
    intptlat = models.CharField(max_length=11, **bn)
    intptlon = models.CharField(max_length=12, **bn)
    the_geom = models.MultiPolygonField(srid=4269, **bn)

    class Meta:

        db_table = "cousub"


class Databasechangelog(MetaModel):
    id = models.CharField(max_length=255, primary_key=True)
    author = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    dateexecuted = models.DateTimeField()
    orderexecuted = models.IntegerField()
    exectype = models.CharField(max_length=10)
    md5sum = models.CharField(max_length=35, **bn)
    description = models.CharField(max_length=255, **bn)
    comments = models.CharField(max_length=255, **bn)
    tag = models.CharField(max_length=255, **bn)
    liquibase = models.CharField(max_length=20, **bn)
    contexts = models.CharField(max_length=255, **bn)
    labels = models.CharField(max_length=255, **bn)
    deployment_id = models.CharField(max_length=10, **bn)

    class Meta:

        db_table = "databasechangelog"


class Databasechangeloglock(MetaModel):
    id = models.IntegerField(primary_key=True)
    locked = models.BooleanField()
    lockgranted = models.DateTimeField(**bn)
    lockedby = models.CharField(max_length=255, **bn)

    class Meta:

        db_table = "databasechangeloglock"


class Datastreams(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    sensor = models.ForeignKey("Sensors", models.DO_NOTHING)
    thing = models.ForeignKey("Things", models.DO_NOTHING)
    proximate_feature = models.ForeignKey("Features", models.DO_NOTHING, **bn)
    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    result_type = models.JSONField(**bn)
    result_encoding = models.JSONField(**bn)
    properties = models.JSONField(**bn)
    phenomenon_time_start = models.DateTimeField(**bn)
    phenomenon_time_end = models.DateTimeField(**bn)
    result_time_start = models.DateTimeField(**bn)
    result_time_end = models.DateTimeField(**bn)
    observed_area = models.GeometryField(**bn)
    last_foi_id = models.BigIntegerField(**bn)

    class Meta:

        db_table = "datastreams"
        verbose_name_plural = db_table


class DatastreamsFeaturesUltimate(MetaModel):
    pk = models.CompositePrimaryKey("datastream_id", "feature_id")
    datastream = models.ForeignKey(Datastreams, models.DO_NOTHING)
    feature = models.ForeignKey("Features", models.DO_NOTHING)

    class Meta:

        db_table = "datastreams_features_ultimate"


class DatastreamsObservedProperties(MetaModel):
    pk = models.CompositePrimaryKey("observed_property_id", "datastream_id")
    observed_property = models.ForeignKey("ObservedProperties", models.DO_NOTHING)
    datastream = models.ForeignKey(Datastreams, models.DO_NOTHING)

    class Meta:

        db_table = "datastreams_observed_properties"
        verbose_name_plural = db_table


class DirectionLookup(MetaModel):
    name = models.CharField(primary_key=True, max_length=20)
    abbrev = models.CharField(max_length=3, **bn)

    class Meta:

        db_table = "direction_lookup"


class Edges(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    statefp = models.CharField(max_length=2, **bn)
    countyfp = models.CharField(max_length=3, **bn)
    tlid = models.BigIntegerField(**bn)
    tfidl = models.DecimalField(max_digits=10, decimal_places=0, **bn)
    tfidr = models.DecimalField(max_digits=10, decimal_places=0, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    fullname = models.CharField(max_length=100, **bn)
    smid = models.CharField(max_length=22, **bn)
    lfromadd = models.CharField(max_length=12, **bn)
    ltoadd = models.CharField(max_length=12, **bn)
    rfromadd = models.CharField(max_length=12, **bn)
    rtoadd = models.CharField(max_length=12, **bn)
    zipl = models.CharField(max_length=5, **bn)
    zipr = models.CharField(max_length=5, **bn)
    featcat = models.CharField(max_length=1, **bn)
    hydroflg = models.CharField(max_length=1, **bn)
    railflg = models.CharField(max_length=1, **bn)
    roadflg = models.CharField(max_length=1, **bn)
    olfflg = models.CharField(max_length=1, **bn)
    passflg = models.CharField(max_length=1, **bn)
    divroad = models.CharField(max_length=1, **bn)
    exttyp = models.CharField(max_length=1, **bn)
    ttyp = models.CharField(max_length=1, **bn)
    deckedroad = models.CharField(max_length=1, **bn)
    artpath = models.CharField(max_length=1, **bn)
    persist = models.CharField(max_length=1, **bn)
    gcseflg = models.CharField(max_length=1, **bn)
    offsetl = models.CharField(max_length=1, **bn)
    offsetr = models.CharField(max_length=1, **bn)
    tnidf = models.DecimalField(max_digits=10, decimal_places=0, **bn)
    tnidt = models.DecimalField(max_digits=10, decimal_places=0, **bn)
    the_geom = models.MultiLineStringField(srid=4269, **bn)

    class Meta:

        db_table = "edges"
        verbose_name_plural = db_table


class Faces(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    tfid = models.DecimalField(max_digits=10, decimal_places=0, **bn)
    statefp00 = models.CharField(max_length=2, **bn)
    countyfp00 = models.CharField(max_length=3, **bn)
    tractce00 = models.CharField(max_length=6, **bn)
    blkgrpce00 = models.CharField(max_length=1, **bn)
    blockce00 = models.CharField(max_length=4, **bn)
    cousubfp00 = models.CharField(max_length=5, **bn)
    submcdfp00 = models.CharField(max_length=5, **bn)
    conctyfp00 = models.CharField(max_length=5, **bn)
    placefp00 = models.CharField(max_length=5, **bn)
    aiannhfp00 = models.CharField(max_length=5, **bn)
    aiannhce00 = models.CharField(max_length=4, **bn)
    comptyp00 = models.CharField(max_length=1, **bn)
    trsubfp00 = models.CharField(max_length=5, **bn)
    trsubce00 = models.CharField(max_length=3, **bn)
    anrcfp00 = models.CharField(max_length=5, **bn)
    elsdlea00 = models.CharField(max_length=5, **bn)
    scsdlea00 = models.CharField(max_length=5, **bn)
    unsdlea00 = models.CharField(max_length=5, **bn)
    uace00 = models.CharField(max_length=5, **bn)
    cd108fp = models.CharField(max_length=2, **bn)
    sldust00 = models.CharField(max_length=3, **bn)
    sldlst00 = models.CharField(max_length=3, **bn)
    vtdst00 = models.CharField(max_length=6, **bn)
    zcta5ce00 = models.CharField(max_length=5, **bn)
    tazce00 = models.CharField(max_length=6, **bn)
    ugace00 = models.CharField(max_length=5, **bn)
    puma5ce00 = models.CharField(max_length=5, **bn)
    statefp = models.CharField(max_length=2, **bn)
    countyfp = models.CharField(max_length=3, **bn)
    tractce = models.CharField(max_length=6, **bn)
    blkgrpce = models.CharField(max_length=1, **bn)
    blockce = models.CharField(max_length=4, **bn)
    cousubfp = models.CharField(max_length=5, **bn)
    submcdfp = models.CharField(max_length=5, **bn)
    conctyfp = models.CharField(max_length=5, **bn)
    placefp = models.CharField(max_length=5, **bn)
    aiannhfp = models.CharField(max_length=5, **bn)
    aiannhce = models.CharField(max_length=4, **bn)
    comptyp = models.CharField(max_length=1, **bn)
    trsubfp = models.CharField(max_length=5, **bn)
    trsubce = models.CharField(max_length=3, **bn)
    anrcfp = models.CharField(max_length=5, **bn)
    ttractce = models.CharField(max_length=6, **bn)
    tblkgpce = models.CharField(max_length=1, **bn)
    elsdlea = models.CharField(max_length=5, **bn)
    scsdlea = models.CharField(max_length=5, **bn)
    unsdlea = models.CharField(max_length=5, **bn)
    uace = models.CharField(max_length=5, **bn)
    cd111fp = models.CharField(max_length=2, **bn)
    sldust = models.CharField(max_length=3, **bn)
    sldlst = models.CharField(max_length=3, **bn)
    vtdst = models.CharField(max_length=6, **bn)
    zcta5ce = models.CharField(max_length=5, **bn)
    tazce = models.CharField(max_length=6, **bn)
    ugace = models.CharField(max_length=5, **bn)
    puma5ce = models.CharField(max_length=5, **bn)
    csafp = models.CharField(max_length=3, **bn)
    cbsafp = models.CharField(max_length=5, **bn)
    metdivfp = models.CharField(max_length=5, **bn)
    cnectafp = models.CharField(max_length=3, **bn)
    nectafp = models.CharField(max_length=5, **bn)
    nctadvfp = models.CharField(max_length=5, **bn)
    lwflag = models.CharField(max_length=1, **bn)
    offset = models.CharField(max_length=1, **bn)
    atotal = models.FloatField(**bn)
    intptlat = models.CharField(max_length=11, **bn)
    intptlon = models.CharField(max_length=12, **bn)
    the_geom = models.MultiPolygonField(srid=4269, **bn)
    tractce20 = models.CharField(max_length=6, **bn)
    blkgrpce20 = models.CharField(max_length=1, **bn)
    blockce20 = models.CharField(max_length=4, **bn)
    countyfp20 = models.CharField(max_length=3, **bn)
    statefp20 = models.CharField(max_length=2, **bn)

    class Meta:

        db_table = "faces"
        verbose_name_plural = db_table


class Featnames(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    tlid = models.BigIntegerField(**bn)
    fullname = models.CharField(max_length=100, **bn)
    name = models.CharField(max_length=100, **bn)
    predirabrv = models.CharField(max_length=15, **bn)
    pretypabrv = models.CharField(max_length=50, **bn)
    prequalabr = models.CharField(max_length=15, **bn)
    sufdirabrv = models.CharField(max_length=15, **bn)
    suftypabrv = models.CharField(max_length=50, **bn)
    sufqualabr = models.CharField(max_length=15, **bn)
    predir = models.CharField(max_length=2, **bn)
    pretyp = models.CharField(max_length=3, **bn)
    prequal = models.CharField(max_length=2, **bn)
    sufdir = models.CharField(max_length=2, **bn)
    suftyp = models.CharField(max_length=3, **bn)
    sufqual = models.CharField(max_length=2, **bn)
    linearid = models.CharField(max_length=22, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    paflag = models.CharField(max_length=1, **bn)
    statefp = models.CharField(max_length=2, **bn)

    class Meta:

        db_table = "featnames"
        verbose_name_plural = db_table


class FeatureTypes(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    properties = models.JSONField(**bn)

    class Meta:

        db_table = "feature_types"
        verbose_name_plural = db_table


class Features(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    encoding_type = models.TextField(**bn)
    feature = models.TextField(**bn)
    geom = models.GeometryField(**bn)
    properties = models.JSONField(**bn)
    creator_sampling = models.ForeignKey("Samplings", models.DO_NOTHING, **bn)

    class Meta:

        db_table = "features"
        verbose_name_plural = db_table


class FeaturesFeatureTypes(MetaModel):
    pk = models.CompositePrimaryKey("feature_id", "feature_type_id")
    feature = models.ForeignKey(Features, models.DO_NOTHING)
    feature_type = models.ForeignKey(FeatureTypes, models.DO_NOTHING)

    class Meta:

        db_table = "features_feature_types"
        verbose_name_plural = db_table


class GeocodeSettings(MetaModel):
    name = models.TextField(primary_key=True)
    setting = models.TextField(**bn)
    unit = models.TextField(**bn)
    category = models.TextField(**bn)
    short_desc = models.TextField(**bn)

    class Meta:

        db_table = "geocode_settings"
        verbose_name_plural = db_table


class GeocodeSettingsDefault(MetaModel):
    name = models.TextField(primary_key=True)
    setting = models.TextField(**bn)
    unit = models.TextField(**bn)
    category = models.TextField(**bn)
    short_desc = models.TextField(**bn)

    class Meta:

        db_table = "geocode_settings_default"


class HistLocations(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    thing = models.ForeignKey("Things", models.DO_NOTHING)
    time = models.DateTimeField(**bn)

    class Meta:

        db_table = "hist_locations"


class Layer(MetaModel):
    pk = models.CompositePrimaryKey("topology_id", "layer_id")
    topology = models.ForeignKey("Topology", models.DO_NOTHING)
    layer_id = models.IntegerField()
    schema_name = models.CharField()
    table_name = models.CharField()
    feature_column = models.CharField()
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(**bn)

    class Meta:

        db_table = "layer"
        unique_together = (("schema_name", "table_name", "feature_column"),)


class LoaderLookuptables(MetaModel):
    process_order = models.IntegerField()
    lookup_name = models.TextField(
        primary_key=True,
        db_comment="This is the table name to inherit from and suffix of resulting output table -- how the table will be named --  edges here would mean -- ma_edges , pa_edges etc. except in the case of national tables. national level tables have no prefix",
    )
    table_name = models.TextField(
        blank=True,
        null=True,
        db_comment="suffix of the tables to load e.g.  edges would load all tables like *edges.dbf(shp)  -- so tl_2010_42129_edges.dbf .  ",
    )
    single_mode = models.BooleanField()
    load = models.BooleanField(
        db_comment="Whether or not to load the table.  For states and zcta5 (you may just want to download states10, zcta510 nationwide file manually) load your own into a single table that inherits from tiger.states, tiger.zcta5.  You'll get improved performance for some geocoding cases."
    )
    level_county = models.BooleanField()
    level_state = models.BooleanField()
    level_nation = models.BooleanField(
        db_comment="These are tables that contain all data for the whole US so there is just a single file"
    )
    post_load_process = models.TextField(**bn)
    single_geom_mode = models.BooleanField(**bn)
    insert_mode = models.CharField(max_length=1)
    pre_load_process = models.TextField(**bn)
    columns_exclude = models.TextField(
        blank=True,
        null=True,
        db_comment="List of columns to exclude as an array. This is excluded from both input table and output table and rest of columns remaining are assumed to be in same order in both tables. gid, geoid,cpi,suffix1ce are excluded if no columns are specified.",
    )  # This field type is a guess.
    website_root_override = models.TextField(
        blank=True,
        null=True,
        db_comment="Path to use for wget instead of that specified in year table.  Needed currently for zcta where they release that only for 2000 and 2010",
    )

    class Meta:

        db_table = "loader_lookuptables"
        verbose_name_plural = db_table


class LoaderPlatform(MetaModel):
    os = models.CharField(primary_key=True, max_length=50)
    declare_sect = models.TextField(**bn)
    pgbin = models.TextField(**bn)
    wget = models.TextField(**bn)
    unzip_command = models.TextField(**bn)
    psql = models.TextField(**bn)
    path_sep = models.TextField(**bn)
    loader = models.TextField(**bn)
    environ_set_command = models.TextField(**bn)
    county_process_command = models.TextField(**bn)

    class Meta:

        db_table = "loader_platform"


class LoaderVariables(MetaModel):
    tiger_year = models.CharField(primary_key=True, max_length=4)
    website_root = models.TextField(**bn)
    staging_fold = models.TextField(**bn)
    data_schema = models.TextField(**bn)
    staging_schema = models.TextField(**bn)

    class Meta:

        db_table = "loader_variables"
        verbose_name_plural = db_table


class Locations(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    encoding_type = models.TextField(**bn)
    location = models.TextField(**bn)
    geom = models.GeometryField(**bn)
    properties = models.JSONField(**bn)

    class Meta:

        db_table = "locations"
        verbose_name_plural = db_table


class LocationsHistLocations(MetaModel):
    pk = models.CompositePrimaryKey("location_id", "hist_location_id")
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    hist_location = models.ForeignKey(HistLocations, models.DO_NOTHING)

    class Meta:

        db_table = "locations_hist_locations"
        verbose_name_plural = db_table


class Observations(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    datastream = models.ForeignKey(Datastreams, models.DO_NOTHING)
    feature = models.ForeignKey(Features, models.DO_NOTHING, **bn)
    phenomenon_time_start = models.DateTimeField(**bn)
    phenomenon_time_end = models.DateTimeField(**bn)
    result_time = models.DateTimeField(**bn)
    result_type = models.SmallIntegerField(**bn)
    result_number = models.FloatField(**bn)
    result_boolean = models.BooleanField(**bn)
    result_json = models.JSONField(**bn)
    result_string = models.TextField(**bn)
    valid_time_start = models.DateTimeField(**bn)
    valid_time_end = models.DateTimeField(**bn)
    properties = models.JSONField(**bn)

    class Meta:

        db_table = "observations"
        verbose_name_plural = db_table


class ObservedProperties(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    properties = models.JSONField(**bn)

    class Meta:

        db_table = "observed_properties"
        verbose_name_plural = db_table


class PagcGaz(MetaModel):
    seq = models.IntegerField(**bn)
    word = models.TextField(**bn)
    stdword = models.TextField(**bn)
    token = models.IntegerField(**bn)
    is_custom = models.BooleanField()

    class Meta:

        db_table = "pagc_gaz"


class PagcLex(MetaModel):
    seq = models.IntegerField(**bn)
    word = models.TextField(**bn)
    stdword = models.TextField(**bn)
    token = models.IntegerField(**bn)
    is_custom = models.BooleanField()

    class Meta:

        db_table = "pagc_lex"


class PagcRules(MetaModel):
    rule = models.TextField(**bn)
    is_custom = models.BooleanField(**bn)

    class Meta:

        db_table = "pagc_rules"
        verbose_name_plural = db_table


class Place(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    statefp = models.CharField(max_length=2, **bn)
    placefp = models.CharField(max_length=5, **bn)
    placens = models.CharField(max_length=8, **bn)
    plcidfp = models.CharField(**bn, max_length=7)
    name = models.CharField(max_length=100, **bn)
    namelsad = models.CharField(max_length=100, **bn)
    lsad = models.CharField(max_length=2, **bn)
    classfp = models.CharField(max_length=2, **bn)
    cpi = models.CharField(max_length=1, **bn)
    pcicbsa = models.CharField(max_length=1, **bn)
    pcinecta = models.CharField(max_length=1, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    funcstat = models.CharField(max_length=1, **bn)
    aland = models.BigIntegerField(**bn)
    awater = models.BigIntegerField(**bn)
    intptlat = models.CharField(max_length=11, **bn)
    intptlon = models.CharField(max_length=12, **bn)
    the_geom = models.MultiPolygonField(srid=4269, **bn)

    class Meta:

        db_table = "place"


class PlaceLookup(MetaModel):
    pk = models.CompositePrimaryKey("st_code", "pl_code")
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, **bn)
    pl_code = models.IntegerField()
    name = models.CharField(max_length=90, **bn)

    class Meta:

        db_table = "place_lookup"


class PreparationProcedures(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    properties = models.JSONField(**bn)

    class Meta:

        db_table = "preparation_procedures"
        verbose_name_plural = db_table


class PreparationSteps(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    feature = models.ForeignKey(Features, models.DO_NOTHING)
    preparation_procedure = models.ForeignKey(PreparationProcedures, models.DO_NOTHING)
    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    properties = models.JSONField(**bn)
    time = models.DateTimeField(**bn)

    class Meta:

        db_table = "preparation_steps"
        verbose_name_plural = db_table


class RelatedDatastreams(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    source_datastream = models.ForeignKey(Datastreams, models.DO_NOTHING)
    target_datastream = models.ForeignKey(
        Datastreams,
        models.DO_NOTHING,
        related_name="relateddatastreams_target_datastream_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey("RelationRoles", models.DO_NOTHING)
    external_target = models.TextField(**bn)

    class Meta:

        db_table = "related_datastreams"
        verbose_name_plural = db_table


class RelatedFeatures(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    source_feature = models.ForeignKey(Features, models.DO_NOTHING)
    target_feature = models.ForeignKey(
        Features,
        models.DO_NOTHING,
        related_name="relatedfeatures_target_feature_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey("RelationRoles", models.DO_NOTHING)
    external_target = models.TextField(**bn)

    class Meta:

        db_table = "related_features"
        verbose_name_plural = db_table


class RelatedObservations(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    source_observation = models.ForeignKey(Observations, models.DO_NOTHING)
    target_observation = models.ForeignKey(
        Observations,
        models.DO_NOTHING,
        related_name="relatedobservations_target_observation_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey("RelationRoles", models.DO_NOTHING)
    external_target = models.TextField(**bn)

    class Meta:

        db_table = "related_observations"
        verbose_name_plural = db_table


class RelatedThings(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    source_thing = models.ForeignKey("Things", models.DO_NOTHING)
    target_thing = models.ForeignKey(
        "Things",
        models.DO_NOTHING,
        related_name="relatedthings_target_thing_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey("RelationRoles", models.DO_NOTHING)
    external_target = models.TextField(**bn)

    class Meta:

        db_table = "related_things"
        verbose_name_plural = db_table


class RelationRoles(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    inverse_name = models.TextField(**bn)
    inverse_definition = models.TextField(**bn)
    description = models.TextField(**bn)
    properties = models.JSONField(**bn)

    class Meta:

        db_table = "relation_roles"
        verbose_name_plural = db_table


class SamplerSamplingProcedure(MetaModel):
    pk = models.CompositePrimaryKey("sampler_id", "procedure_id")
    sampler = models.ForeignKey("Samplers", models.DO_NOTHING)
    procedure = models.ForeignKey("SamplingProcedures", models.DO_NOTHING)

    class Meta:

        db_table = "sampler_sampling_procedure"


class Samplers(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    properties = models.JSONField(**bn)
    sampler_type = models.TextField(**bn)

    class Meta:

        db_table = "samplers"
        verbose_name_plural = db_table


class SamplingProcedures(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    properties = models.JSONField(**bn)

    class Meta:

        db_table = "sampling_procedures"
        verbose_name_plural = db_table


class Samplings(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    thing = models.ForeignKey("Things", models.DO_NOTHING, **bn)
    sampled_feature = models.ForeignKey(Features, models.DO_NOTHING)
    sampler = models.ForeignKey(Samplers, models.DO_NOTHING, **bn)
    procedure = models.ForeignKey(SamplingProcedures, models.DO_NOTHING, **bn)
    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    encoding_type = models.TextField(**bn)
    location = models.TextField(**bn)
    geom = models.GeometryField(**bn)
    properties = models.JSONField(**bn)
    sampling_time_start = models.DateTimeField(**bn)
    sampling_time_end = models.DateTimeField(**bn)

    class Meta:

        db_table = "samplings"
        verbose_name_plural = db_table


class SecondaryUnitLookup(MetaModel):
    name = models.CharField(primary_key=True, max_length=20)
    abbrev = models.CharField(max_length=5, **bn)

    class Meta:

        db_table = "secondary_unit_lookup"


class Sensors(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    encoding_type = models.TextField(**bn)
    metadata = models.JSONField(**bn)
    properties = models.JSONField(**bn)

    class Meta:

        db_table = "sensors"
        verbose_name_plural = db_table


class State(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    region = models.CharField(max_length=2, **bn)
    division = models.CharField(max_length=2, **bn)
    statefp = models.CharField(**bn, max_length=2)
    statens = models.CharField(max_length=8, **bn)
    stusps = models.CharField(unique=True, max_length=2)
    name = models.CharField(max_length=100, **bn)
    lsad = models.CharField(max_length=2, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    funcstat = models.CharField(max_length=1, **bn)
    aland = models.BigIntegerField(**bn)
    awater = models.BigIntegerField(**bn)
    intptlat = models.CharField(max_length=11, **bn)
    intptlon = models.CharField(max_length=12, **bn)
    the_geom = models.MultiPolygonField(srid=4269, **bn)

    class Meta:

        db_table = "state"


class StateLookup(MetaModel):
    st_code = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=40, **bn)
    abbrev = models.CharField(unique=True, max_length=3, **bn)
    statefp = models.CharField(unique=True, max_length=2, **bn)

    class Meta:

        db_table = "state_lookup"


class StreetTypeLookup(MetaModel):
    name = models.CharField(primary_key=True, max_length=50)
    abbrev = models.CharField(max_length=50, **bn)
    is_hw = models.BooleanField()

    class Meta:

        db_table = "street_type_lookup"


class Tabblock(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    statefp = models.CharField(max_length=2, **bn)
    countyfp = models.CharField(max_length=3, **bn)
    tractce = models.CharField(max_length=6, **bn)
    blockce = models.CharField(max_length=4, **bn)
    tabblock_id = models.CharField(**bn, max_length=16)
    name = models.CharField(max_length=20, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    ur = models.CharField(max_length=1, **bn)
    uace = models.CharField(max_length=5, **bn)
    funcstat = models.CharField(max_length=1, **bn)
    aland = models.FloatField(**bn)
    awater = models.FloatField(**bn)
    intptlat = models.CharField(max_length=11, **bn)
    intptlon = models.CharField(max_length=12, **bn)
    the_geom = models.MultiPolygonField(srid=4269, **bn)

    class Meta:

        db_table = "tabblock"


class Tabblock20(MetaModel):
    statefp = models.CharField(max_length=2, **bn)
    countyfp = models.CharField(max_length=3, **bn)
    tractce = models.CharField(max_length=6, **bn)
    blockce = models.CharField(max_length=4, **bn)
    geoid = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=10, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    ur = models.CharField(max_length=1, **bn)
    uace = models.CharField(max_length=5, **bn)
    uatype = models.CharField(max_length=1, **bn)
    funcstat = models.CharField(max_length=1, **bn)
    aland = models.FloatField(**bn)
    awater = models.FloatField(**bn)
    intptlat = models.CharField(max_length=11, **bn)
    intptlon = models.CharField(max_length=12, **bn)
    the_geom = models.MultiPolygonField(srid=4269, **bn)
    housing = models.FloatField(**bn)
    pop = models.FloatField(**bn)

    class Meta:

        db_table = "tabblock20"


class Things(MetaModel):
    id = models.PositiveBigIntegerField(primary_key=True)

    name = models.TextField(**bn)
    definition = models.TextField(**bn)
    description = models.TextField(**bn)
    properties = models.JSONField(**bn)

    class Meta:

        db_table = "things"
        verbose_name_plural = db_table


class ThingsLocations(MetaModel):
    pk = models.CompositePrimaryKey("thing_id", "location_id")
    thing = models.ForeignKey(Things, models.DO_NOTHING)
    location = models.ForeignKey(Locations, models.DO_NOTHING)

    class Meta:

        db_table = "things_locations"
        verbose_name_plural = db_table


class Topology(MetaModel):
    name = models.CharField(unique=True)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:

        db_table = "topology"


class Tract(MetaModel):
    gid = models.PositiveIntegerField(**bn)
    statefp = models.CharField(max_length=2, **bn)
    countyfp = models.CharField(max_length=3, **bn)
    tractce = models.CharField(max_length=6, **bn)
    tract_id = models.CharField(**bn, max_length=11)
    name = models.CharField(max_length=7, **bn)
    namelsad = models.CharField(max_length=20, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    funcstat = models.CharField(max_length=1, **bn)
    aland = models.FloatField(**bn)
    awater = models.FloatField(**bn)
    intptlat = models.CharField(max_length=11, **bn)
    intptlon = models.CharField(max_length=12, **bn)
    the_geom = models.MultiPolygonField(srid=4269, **bn)

    class Meta:

        db_table = "tract"


class Zcta5(MetaModel):
    pk = models.CompositePrimaryKey("zcta5ce", "statefp")
    gid = models.PositiveIntegerField(**bn)
    statefp = models.CharField(max_length=2)
    zcta5ce = models.CharField(max_length=5)
    classfp = models.CharField(max_length=2, **bn)
    mtfcc = models.CharField(max_length=5, **bn)
    funcstat = models.CharField(max_length=1, **bn)
    aland = models.FloatField(**bn)
    awater = models.FloatField(**bn)
    intptlat = models.CharField(max_length=11, **bn)
    intptlon = models.CharField(max_length=12, **bn)
    partflg = models.CharField(max_length=1, **bn)
    the_geom = models.MultiPolygonField(srid=4269, **bn)

    class Meta:

        db_table = "zcta5"


class ZipLookup(MetaModel):
    zip = models.IntegerField(primary_key=True)
    st_code = models.IntegerField(**bn)
    state = models.CharField(max_length=2, **bn)
    co_code = models.IntegerField(**bn)
    county = models.CharField(max_length=90, **bn)
    cs_code = models.IntegerField(**bn)
    cousub = models.CharField(max_length=90, **bn)
    pl_code = models.IntegerField(**bn)
    place = models.CharField(max_length=90, **bn)
    cnt = models.IntegerField(**bn)

    class Meta:

        db_table = "zip_lookup"


class ZipLookupAll(MetaModel):
    zip = models.IntegerField(**bn)
    st_code = models.IntegerField(**bn)
    state = models.CharField(max_length=2, **bn)
    co_code = models.IntegerField(**bn)
    county = models.CharField(max_length=90, **bn)
    cs_code = models.IntegerField(**bn)
    cousub = models.CharField(max_length=90, **bn)
    pl_code = models.IntegerField(**bn)
    place = models.CharField(max_length=90, **bn)
    cnt = models.IntegerField(**bn)

    class Meta:

        db_table = "zip_lookup_all"


class ZipLookupBase(MetaModel):
    zip = models.CharField(primary_key=True, max_length=5)
    state = models.CharField(max_length=40, **bn)
    county = models.CharField(max_length=90, **bn)
    city = models.CharField(max_length=90, **bn)
    statefp = models.CharField(max_length=2, **bn)

    class Meta:

        db_table = "zip_lookup_base"


class ZipState(MetaModel):
    pk = models.CompositePrimaryKey("zip", "stusps")
    zip = models.CharField(max_length=5)
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, **bn)

    class Meta:

        db_table = "zip_state"


class ZipStateLoc(MetaModel):
    pk = models.CompositePrimaryKey("zip", "stusps", "place")
    zip = models.CharField(max_length=5)
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, **bn)
    place = models.CharField(max_length=100)

    class Meta:

        db_table = "zip_state_loc"
