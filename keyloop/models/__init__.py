import pymodm
from pymodm import fields
from keyloop.models.base import User, UserExtension


class DynamicModels:
    @property
    def User(self):
        custom_fields = [
            f for f in UserExtension.objects.all()  # pylint: disable=maybe-no-member
        ]

        _fields_args = dict(__module__=User.__module__)

        for c in custom_fields:
            _fields_args.update({c.field: getattr(fields, c.field_type)()})

        return type("User", (User,), _fields_args)


def includeme(config):
    settings = config.registry.settings
    mongo_uri = settings.get("mongo.uri")
    pymodm.connection.connect(mongo_uri, alias="keyloop")

    config.registry.DynamicModels = DynamicModels()
