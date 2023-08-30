# API Maps

* provider: mapsscript
* mapserver-cgi (ubuntu) needs to be installed
* shapefile polygon tested successfully
* styles work via SLD. The layername in the resource has to match the layer name in the SLD (`/NamedLayer/Name`)

CLI test: `mapserv -nh "QUERY_STRING=map=/data/mapfile.map&mode=map&REQUEST=GetMap&LAYERS=my_shapefile" > /data/test1.png`

## combining with API Features

* set up a second provider --> Note that it will not show in the landing page (most likely a bug/limitation)

Test URLs:

* http://localhost:5000/collections/countries1/items
* http://localhost:5000/collections/countries1/map?f=png

## config snippet

```yaml
resources:
    countries1:
        type: collection
        title: World Countries (MapScript)
        description: World Countries (MapScript)
        keywords:
            - MapScript
            - countries
            - Feature
            - Maps
        extents:
            spatial:
                bbox: [-180,-90, 180, 90]
                crs: http://www.opengis.net/def/crs/OGC/1.3/CRS84
        providers:
            - type: map
              name: MapScript
              data: postgresql://postgres:postgres@postgis-1:5432/gis
              options:
                  type: MS_LAYER_POLYGON
                  layer: countries1
                  style: /data/world/world_polygon1.sld
              format:
                  name: png
                  mimetype: image/png
            - type: feature
              name: PostgreSQL
              data:
                host: postgis-1
                port: 5432 # Default 5432 if not provided
                dbname: gis
                user: postgres
                password: postgres
                search_path: [public]
              id_field: fid
              table: countries1
              geom_field: geom
 
```

## common issues

### blank map

possible reasons:

* non-matching geometry type defined in the configuration of the resource: MS_LAYER_POINT, MS_LAYER_LINE, MS_LAYER_POLYGON
* layer name not matching the SLD file
* SQL connection wrong
* data directory wrong (has to be relative to pygeoapi workdir, or absolute)
* SLD file path wrong (has to be relative to pygeoapi workdir, or absolute)
