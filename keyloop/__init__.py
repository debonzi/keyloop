from pyramid.config import Configurator
from pyramid.response import Response

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy


def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        config.include("keyloop.models")
        config.include("cornice")

        config.include("keyloop.api", route_prefix="/api")

        # Security policies
        authn_policy = AuthTktAuthenticationPolicy(
            "sekret",
            hashalg="sha512",
            # callback=groupfinder,
        )
        authz_policy = ACLAuthorizationPolicy()
        config.set_authentication_policy(authn_policy)
        config.set_authorization_policy(authz_policy)

        app = config.make_wsgi_app()
    return app
