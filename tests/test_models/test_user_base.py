import pytest
import transaction
from sqlalchemy.exc import IntegrityError

from keyloop.models import Credential, DBSession
from tests.factories import CredentialFactory


def test_credential_password():
    cred = CredentialFactory(password="123123123a")
    transaction.commit()
    DBSession.add(cred)
    restored_cred = Credential.query.filter_by(uuid=cred.uuid).first()

    assert restored_cred._password != "123123123a"  # pylint: disable=protected-access
    assert restored_cred.password_check("123123123a") is True


def test_create_credential_with_only_username():
    cred = Credential(_password="123456a", username="jessica_miller")

    DBSession.add(cred)
    transaction.commit()

    restored_cred = Credential.query.one()

    assert Credential.query.count() == 1
    assert restored_cred.username == "jessica_miller"


def test_create_credential_with_only_msisdn():
    cred = Credential(_password="123456a", msisdn="551199999999",)

    DBSession.add(cred)
    transaction.commit()

    restored_cred = Credential.query.one()

    assert Credential.query.count() == 1
    assert restored_cred.msisdn == "551199999999"


def test_create_credential_with_only_citizen_id():
    cred = Credential(_password="123456a", citizen_id="1234567809",)

    DBSession.add(cred)
    transaction.commit()

    restored_cred = Credential.query.one()

    assert Credential.query.count() == 1
    assert restored_cred.citizen_id == "1234567809"


def test_create_credential_with_only_email():
    cred = Credential(_password="123456a", email="jessica_miller@example.com",)

    DBSession.add(cred)
    transaction.commit()

    restored_cred = Credential.query.one()

    assert Credential.query.count() == 1
    assert restored_cred.email == "jessica_miller@example.com"


def test_create_credential_without_any_field():
    cred = Credential(_password="123456a")

    with pytest.raises(IntegrityError) as t:
        DBSession.add(cred)
        DBSession.flush()

    assert (
        'new row for relation "credentials" violates check constraint "credentials_check"'
        in str(t.value)
    )
