from keyloop.models.realms import Realms


def test_realm_collection_api(testapp):
    Realms("clients", "Clients").create()
    Realms("admins", "Administrators").create()

    res = testapp.get("/api/v1/realms")
    assert res.json == [
        {"description": "", "name": "Clients", "slug": "clients"},
        {"description": "", "name": "Administrators", "slug": "admins"},
    ]


def test_realm_resource_api(testapp):
    Realms("clients", "Clients").create()

    res = testapp.get("/api/v1/realms/clients")
    assert res.json == {
        "description": "",
        "name": "Clients",
        "slug": "clients",
    }


def test_realm_resource_api_404(testapp):
    res = testapp.get("/api/v1/realms/clients", status=404)
    assert res.json == {
        "errors": [
            {
                "description": "Realm does not exist",
                "location": "body",
                "name": "realm_slug",
            }
        ],
        "status": "error",
    }
