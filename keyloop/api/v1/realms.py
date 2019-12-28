from cornice import resource

from pymodm.errors import DoesNotExist

from marshmallow import Schema, fields

from pyramid.security import Allow, Everyone
from pyramid.httpexceptions import HTTPNotFound

from keyloop.models.realms import Realms


class RealmSchema(Schema):
    name = fields.Str()
    slug = fields.Str()
    description = fields.Str(missing="")


class RealmResource(object):
    def __init__(self, request, context=None):
        self.request = request

    def __acl__(self):
        return [(Allow, Everyone, "view")]

    @resource.view(permission="view")
    def collection_get(self):
        realms = Realms.objects.all()
        return RealmSchema().dump(realms, many=True)

    @resource.view(permission="view")
    def get(self):
        realm_slug = self.request.matchdict.get("realm_slug")
        try:
            realm_model = Realms.objects.get({"_id": realm_slug})
        except DoesNotExist:
            self.request.errors.add("body", "realm_slug", "Realm does not exist")
            self.request.errors.status = 404
            return
        return RealmSchema().dump(realm_model)

    # def collection_post(self):
    #     print(self.request.json_body)
    #     _USERS[len(_USERS) + 1] = self.request.json_body
    #     return True


realm_resource = resource.add_resource(
    RealmResource, collection_path="/realms", path="/realms/{realm_slug}",
)


def includeme(config):
    config.add_cornice_resource(realm_resource)
