from marshmallow import Schema, fields


class SchemaRegistry:
    def __init__(self):
        self.registry = {}

    def register(self, json_schema):
        self.registry.update({json_schema["class_name"]: json_schema})

    def get(self, name):
        return self.registry[name]


schema_registry = SchemaRegistry()


def gen_schema(json_schema):
    class_name = json_schema["class_name"]
    attrs = {}
    for name, spec in json_schema["definition"].items():
        field_type = spec["type"]
        field = getattr(fields, field_type)
        value = (
            field(gen_schema(schema_registry.get(spec["schema"])))
            if field_type == "Nested"
            else field()
        )
        attrs.update({name: value})

    return type(class_name, (Schema,), attrs)
