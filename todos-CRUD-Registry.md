# CRUD Registry

Rough tasks:

* extract `self.config["properties]` of `api.py` to dedicated class
* make the transactions thread-safe (e.g. lock object)
* implement a config store so resources survive restarts
* update OpenAPI after each transaction
* implement a good CRUD HTTP API