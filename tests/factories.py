import factory

from keyloop.models import Credential, DBSession, Realm


class CredentialFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Credential
        sqlalchemy_session = DBSession

    password = "123123123a"
    email = factory.LazyAttribute(lambda o: "%s@geru.com.br" % factory.Faker("name"))


class RealmFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Realm
        sqlalchemy_session = DBSession

    name = factory.Faker("name")
    slug = factory.LazyAttribute(lambda s: s.name.lower().replace(" ", "_"))
    description = "test"
