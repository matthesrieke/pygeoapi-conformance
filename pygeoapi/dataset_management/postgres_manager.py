from .resource_manager import ResourceManager
from .crud_resource_registry import CrudResourceRegistryInterface
import threading
import logging

class PostgresResourceManager(ResourceManager):
    
    DUMMY_CONFIG = {
      "type": "collection",
      "title": "World Countries (MapScript)",
      "description": "World Countries (MapScript)",
      "keywords": [
        "MapScript",
        "countries",
        "Feature",
        "Maps"
      ],
      "extents": {
        "spatial": {
          "bbox": [
            -180,
            -90,
            180,
            90
          ],
          "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
        }
      },
      "providers": [
        {
          "type": "map",
          "name": "MapScript",
          "data": "postgresql://postgres:postgres@postgis-1:5432/gis",
          "options": {
            "type": "MS_LAYER_POLYGON",
            "layer": "countries1",
            "style": "/data/world/world_polygon1.sld"
          },
          "format": {
            "name": "png",
            "mimetype": "image/png"
          }
        },
        {
          "type": "feature",
          "name": "PostgreSQL",
          "data": {
            "host": "postgis-1",
            "port": 5432,
            "dbname": "gis",
            "user": "postgres",
            "password": "postgres",
            "search_path": [
              "public"
            ]
          },
          "id_field": "fid",
          "table": "countries1",
          "geom_field": "geom"
        }
      ]
    }
    
    def __init__(self, api_object: CrudResourceRegistryInterface):

        t = threading.Thread(target=self.ingest_vector_data, args=('countries2', '/tmp/data', self.DUMMY_CONFIG, api_object))
        t.start()
    
    def ingest_vector_data(self, collection_name, data_dir, configuration, global_resource_registry: CrudResourceRegistryInterface):
        if global_resource_registry.get_resource_config(collection_name) != None:
            raise Exception(f"Collection with name '{collection_name}' already present")
        
        self.load_and_store_data(data_dir, configuration)
        global_resource_registry.set_resource_config(collection_name, configuration)
        logging.info(f"resource '{collection_name}' registered with configuration: {configuration}")
               
    def load_and_store_data(self, data_dir, configuration):
        pass