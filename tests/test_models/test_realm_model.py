import pytest
import pymongo

from keyloop.models.realms import Realms


def test_realm_config(registry):
    Realms("blog", "Blog").create()
    blog = Realms.objects.get({"_id": "blog"})
    assert blog.name == "Blog"

    Realms("blog", "Blog 2").update()
    blog = Realms.objects.get({"_id": "blog"})
    assert blog.name == "Blog 2"

    with pytest.raises(pymongo.errors.DuplicateKeyError):
        Realms("blog", "Blog").create()
