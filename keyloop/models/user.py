from pymodm import MongoModel, fields

from pymodm.connection import connect
from pymongo import WriteConcern, ReadPreference, ASCENDING, IndexModel

import cryptacular.bcrypt

bcrypt = cryptacular.bcrypt.BCRYPTPasswordManager()


class SimpleUser(MongoModel):
    email = fields.EmailField()
    _password = fields.CharField()

    def _set_password(self, value):
        self._password = bcrypt.encode(value)

    password = property(fset=_set_password)

    def password_check(self, value):
        return bcrypt.check(self._password, value)


class ServerAdmin(SimpleUser):
    class Meta:
        indexes = [IndexModel([("email", ASCENDING)], unique=True)]
        write_concern = WriteConcern(j=True)
        connection_alias = "keyloop"
        collection_name = "ServerAdmin"


class User(SimpleUser):
    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = "keyloop"
        collection_name = "User"
