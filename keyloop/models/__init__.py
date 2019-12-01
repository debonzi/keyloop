import pymodm
from pymodm import fields
from keyloop.models.base import User


def includeme(config):
    settings = config.registry.settings
    mongo_uri = settings.get("mongo.uri")
    pymodm.connection.connect(mongo_uri, alias="keyloop")

    # TODO: The User class must be "Extented" from models.base.User + a mongodb schema describing custom field
    config.registry.User = type(
        "User", (User,), dict(custom=fields.CharField(), __module__=User.__module__)
    )
