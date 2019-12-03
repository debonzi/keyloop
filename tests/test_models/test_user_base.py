import pytest
from keyloop.models.user import UserExtension
from keyloop.models.dynamics.fields import CharField


def test_user_password(registry):
    u = registry.DynamicModels.User(email="debonzi@gmail.com")
    u.password = "123123123a"
    u.save()

    su = registry.DynamicModels.User.objects.get(  # pylint: disable=maybe-no-member
        {"_id": "debonzi@gmail.com"}
    )

    assert su._password != "123123123a"
    assert su.password_check("123123123a") is True


def test_simple_extented_user(registry):
    CharField.create(UserExtension, "custom", required=True)

    registry.DynamicModels.User(email="debonzi@gmail.com", custom="11973102275").save()

    su = registry.DynamicModels.User.objects.get(  # pylint: disable=maybe-no-member
        {"_id": "debonzi@gmail.com"}
    )

    assert su.custom == "11973102275"
