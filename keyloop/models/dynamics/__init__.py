import pymodm
from ..user import User, UserExtension


class DynamicModels:
    def _generate_class(self, name, parent, extension):
        custom_fields = [
            f for f in extension.objects.all()  # pylint: disable=maybe-no-member
        ]

        _fields_args = dict(__module__=parent.__module__)

        for c in custom_fields:
            _fields_args.update(
                {c.field: getattr(pymodm.fields, c.field_type)(**c.field_args)}
            )

        return type(name, (parent,), _fields_args)

    @property
    def User(self):
        return self._generate_class("User", User, UserExtension)
