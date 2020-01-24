from keyloop.models import Credential, DBSession


def test_credential_password():
    cred = Credential(password="123123123a")

    DBSession.add(cred)
    DBSession.flush()

    restored_cred = Credential.query.filter_by(uuid=cred.uuid).first()

    assert restored_cred._password != "123123123a"  # pylint: disable=protected-access
    assert restored_cred.password_check("123123123a") is True
