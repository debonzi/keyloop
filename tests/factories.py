import string
from random import choice, randint

import factory

from keyloop.models import Credential, DBSession, Realm


class CredentialFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Credential
        sqlalchemy_session = DBSession

    password = "".join(
        choice(string.ascii_letters + string.punctuation + string.digits)
        for x in range(randint(8, 16))
    )
    email = "example@example.com"


class RealmFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Realm
        sqlalchemy_session = DBSession

    name = factory.Faker("name")
    slug = factory.LazyAttribute(lambda s: s.name.lower().replace(" ", "_"))
    description = "test"
