from cornice import resource

from pymodm.errors import DoesNotExist
from pyramid.security import Allow, Everyone, remember, forget
from pyramid.httpexceptions import HTTPOk


# from keyloop.models.realms import Realms


policy = dict(
    enabled=True,
    headers=("Content-Type",),
    origins=["*"],
    credentials=True,
    max_age=42,
)


class LoginLogoutFactory:
    def __init__(self, request):
        self.request = request
        realm_slug = self.request.matchdict.get("slug")
        try:
            self.realm = Realms.objects.get({"_id": realm_slug})
        except DoesNotExist:
            self.request.errors.add("body", "realm_slug", "Realm does not exist")
            self.request.errors.status = 404

    def __acl__(self):
        return [(Allow, Everyone, "view")]


class LoginResource:
    def __init__(self, request, context=None):
        self.request = request
        self.context = context

    @resource.view(permission="view")
    def get(self):
        print("HAHAHAHAH", dict(self.request.headers))
        login_headers = remember(self.request, "debonzi")
        print("LOLOLOLOL", login_headers)
        return HTTPOk(json=dict(result="success"), headers=login_headers)


class LogoutResource:
    def __init__(self, request, context=None):
        self.request = request
        self.context = context

    @resource.view(permission="view")
    def get(self):
        logout_headers = forget(self.request)
        return HTTPOk(json=dict(result="success"), headers=logout_headers)


login_resource = resource.add_resource(
    LoginResource,
    path="/realms/{slug}/login",
    factory=LoginLogoutFactory,
    # cors_policy=policy,
    cors_enabled=True,
    cors_origins=["https://accounts.geru-local.com.br"],
    cors_credentials=True,
)

logout_resource = resource.add_resource(
    LogoutResource,
    path="/realms/{slug}/logout",
    factory=LoginLogoutFactory,
    # cors_policy=policy,
    cors_enabled=True,
    cors_origins=["https://accounts.geru-local.com.br"],
    cors_credentials=True,
)


def includeme(config):
    config.add_cornice_resource(login_resource)
    config.add_cornice_resource(logout_resource)
