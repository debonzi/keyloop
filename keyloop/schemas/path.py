import marshmallow


class BasePathSchema(marshmallow.Schema):
    id = marshmallow.fields.UUID(required=True)

    realm_slug = marshmallow.fields.String()
