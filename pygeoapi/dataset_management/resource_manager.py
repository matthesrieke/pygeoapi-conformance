from .crud_resource_registry import CrudResourceRegistry

class ResourceManager:
    """generic ResourceManager ABC"""

    def __init__(self, api_object):
        pass
    
    def ingest_vector_data(self, collection_name, data_dir, configuration,
                           resource_registry: CrudResourceRegistry):
        pass