import pytest
from keyloop import main
from pyramid import paster
from pyramid import testing

from webtest import TestApp

settings = paster.get_appsettings("testing.ini", name="main")
config = testing.setUp(settings=settings)

app_ = main(config, **settings)


@pytest.fixture(scope="function")
def testapp():
    return TestApp(
        app_,
        extra_environ=dict(
            SERVER_NAME="auth.keyloop.org",
            SERVER_PORT="80",
            HTTP_HOST="auth.keyloop.org",
        ),
    )


@pytest.fixture(scope="function")
def registry(testapp):
    return testapp.app.registry
