import os
from pygeoapi.dataset_management.postgres_manager \
    import PostgresResourceManager

prm = PostgresResourceManager(None)

shp_base_dir = "/tmp/test-shapefile"
layer_name = "World_Countries_Generalized"

try:
    prm.ingest_vector_data(layer_name, shp_base_dir, {})
except Exception as e:
    print(e)