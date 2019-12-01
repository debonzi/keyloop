from pymodm import MongoModel, fields

from pymodm.connection import connect
from pymongo.write_concern import WriteConcern

import cryptacular.bcrypt

bcrypt = cryptacular.bcrypt.BCRYPTPasswordManager()


class User(MongoModel):
    email = fields.EmailField(primary_key=True)
    password_ = fields.CharField()

    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, value):
        self.password_ = bcrypt.encode(value)

    def password_check(self, value):
        return bcrypt.check(self.password_, value)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = "keyloop"
        collection_name = "User"
