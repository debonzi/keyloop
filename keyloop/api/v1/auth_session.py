# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import marshmallow

from cornice.resource import resource


from grip.resource import BaseResource
from grip.context import SimpleBaseFactory


class AuthSessionContext(SimpleBaseFactory):
    pass


class CollectionPostSchema(marshmallow.Schema):

    path = marshmallow.fields.Nested(BasePathSchema)
    body = marshmallow.fields.Nested(AuthSessionSchema(exclude=["identity"]))


collection_response_schemas = {200: AuthSessionSchema(exclude=["username", "password"])}


@resource(
    collection_path="/api/v1/{partner_slug}/tokens",
    path="/api/v1/{partner_slug}/tokens/{id}",
    content_type="application/json",
    factory=AuthSessionContext,
)
class AuthSessionAPIv1(BaseResource):

    collection_post_schema = CollectionPostSchema
    collection_response_schemas = collection_response_schemas

    def collection_post(self):

        realm = self.request.validated["path"]["realm_slug"]

        validated = self.request.validated["body"]

        identity = Identity.get_user(validated["username"])

        session = AuthSession(validated["username"], validated["password"], identity)

        remember(validated["username"])

        return session
