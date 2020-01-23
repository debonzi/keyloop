from keyloop.models import Realm, DBSession


def test_realm_config():
    blog = Realm(slug="blog", name="Blog")
    DBSession.add(blog)
    DBSession.flush()

    realm = Realm.query.filter_by(uuid=blog.uuid).first()
    assert realm.name == "Blog"
