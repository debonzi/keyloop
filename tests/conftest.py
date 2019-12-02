import pytest
import pymodm

from keyloop import main
from pyramid import paster
from pyramid import testing

from webtest import TestApp

settings = paster.get_appsettings("testing.ini", name="main")


def _clean_db():
    mdb = pymodm.connection._get_db("keyloop")
    for c in mdb.list_collection_names():
        mdb[c].drop()


@pytest.fixture(scope="session")
def app():
    config = testing.setUp(settings=settings)
    yield main(config, **settings)
    _clean_db()
    testing.tearDown()


@pytest.fixture(scope="function")
def testapp(app):
    testapp_ = TestApp(
        app,
        extra_environ=dict(
            SERVER_NAME="auth.keyloop.org",
            SERVER_PORT="80",
            HTTP_HOST="auth.keyloop.org",
        ),
    )
    _clean_db()
    return testapp_


@pytest.fixture(scope="function")
def registry(app):
    return app.registry
