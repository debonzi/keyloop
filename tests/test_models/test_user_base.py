import transaction

from keyloop.models import Credential, DBSession
from tests.factories import CredentialFactory


def test_credential_password():
    cred = CredentialFactory(password="123123123a")
    transaction.commit()
    DBSession.add(cred)
    restored_cred = Credential.query.filter_by(uuid=cred.uuid).first()

    assert restored_cred._password != "123123123a"  # pylint: disable=protected-access
    assert restored_cred.password_check("123123123a") is True
