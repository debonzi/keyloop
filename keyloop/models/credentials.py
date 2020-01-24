import sqlalchemy as sa

import cryptacular.bcrypt

from .base import Base


__all__ = [
    "Credential",
]

bcrypt = cryptacular.bcrypt.BCRYPTPasswordManager()


class Credential(Base):
    __tablename__ = "credentials"

    def __init__(self, *args, **kwargs):
        password = kwargs.pop("password", None)
        super(Credential, self).__init__(*args, **kwargs)
        if password:
            self.password = password

    email = sa.Column(sa.Text, unique=True)
    _password = sa.Column(sa.Text)

    def _set_password(self, value):
        self._password = bcrypt.encode(value)

    password = property(fset=_set_password)

    def password_check(self, value):
        return bcrypt.check(self._password, value)
