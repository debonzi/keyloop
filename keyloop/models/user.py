from pymodm import MongoModel, fields

from pymodm.connection import connect
from pymongo.write_concern import WriteConcern

import cryptacular.bcrypt

bcrypt = cryptacular.bcrypt.BCRYPTPasswordManager()


class User(MongoModel):
    email = fields.EmailField(primary_key=True)
    _password = fields.CharField()

    def _set_password(self, value):
        self._password = bcrypt.encode(value)

    password = property(fset=_set_password)

    def password_check(self, value):
        return bcrypt.check(self._password, value)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = "keyloop"
        collection_name = "User"


class UserExtension(MongoModel):
    field = fields.CharField(primary_key=True)
    field_type = fields.CharField()
    field_args = fields.DictField(blank=True, default={})

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = "keyloop"
        collection_name = "UserExtension"
