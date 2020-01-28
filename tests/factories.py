import string
from random import choice, randint

import factory

from keyloop.models import Credential, DBSession, Realm


class CredentialFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Credential
        sqlalchemy_session = DBSession

    name = factory.Faker("name")
    username = factory.LazyAttribute(lambda s: s.name.lower().replace(" ", "_"))
    msisdn = "551199999999"
    citizen_id = "1234567809"
    additional_data = {"key1": "value1"}
    password = "".join(
        choice(string.ascii_letters + string.punctuation + string.digits)
        for x in range(randint(8, 16))
    )
    email = factory.LazyAttribute(
        lambda n: "{}@example.com".format(n.name.lower().replace(" ", "_"))
    )


class RealmFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Realm
        sqlalchemy_session = DBSession

    name = factory.Faker("name")
    slug = factory.LazyAttribute(lambda s: s.name.lower().replace(" ", "_"))
    description = "test"
