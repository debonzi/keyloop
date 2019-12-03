import pymodm
from pymodm import fields
from keyloop.models.dynamics import DynamicModels


def includeme(config):
    settings = config.registry.settings
    mongo_uri = settings.get("mongo.uri")
    pymodm.connection.connect(mongo_uri, alias="keyloop")

    config.registry.DynamicModels = DynamicModels()
