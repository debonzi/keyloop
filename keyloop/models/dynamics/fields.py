class BaseField:
    FIELD_TYPE = ""

    @classmethod
    def create(cls, extension_class, field_name, **kwargs):
        """Create a new Field instance.

        :parameters:
          - `extension_class`: The extension model class that will receive this
             field.
          - `field_name`: Field name
          - `blank`: If ``True``, allow this field to have an empty value.
          - `required`: If ``True``, do not allow this field to be unspecified.
          - `default`: The default value to use for this field if no other value
            has been given. If ``default`` is callable, then the return value of
            ``default()`` will be used as the default value.
          - `choices`: A list of possible values for the field. This can be a
            flat list, or a list of 2-tuples consisting of an allowed field
            value and a human-readable version of that value.
          - `validators`: A list of callables used to validate this Field's
            value.
        """
        extension_class(
            field="custom", field_type=cls.FIELD_TYPE, field_args=kwargs
        ).save()


class CharField(BaseField):
    FIELD_TYPE = "CharField"

    # Is there a way to avoid have this method here just to write a proper docstring?
    @classmethod
    def create(cls, extension_class, field_name, **kwargs):
        """
        :parameters:
            - `verbose_name`: A human-readable name for the Field.
            - `min_length`: The required minimum length of the string.
            - `max_length`: The required maximum length of the string.

        .. seealso:: create for
                        :class:`~keyloop.models.dynamics.BaseField`

        """
        super().create(extension_class, field_name, **kwargs)
