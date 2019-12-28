def test_user_password(registry):
    u = registry.DynamicModels.User(email="debonzi@email.com")
    u.password = "123123123a"
    u.save()

    su = registry.DynamicModels.User.objects.get(  # pylint: disable=maybe-no-member
        {"email": "debonzi@email.com"}
    )

    assert su._password != "123123123a"
    assert su.password_check("123123123a") is True


def test_simple_extented_user(registry):
    from dyn_pymodm.fields import CharField

    registry.DynamicModels.user_handler.add_field(
        CharField(name="custom", required=True).serial()
    )

    registry.DynamicModels.User(email="debonzi@email.com", custom="11973102275").save()

    su = registry.DynamicModels.User.objects.get(  # pylint: disable=maybe-no-member
        {"email": "debonzi@email.com"}
    )

    assert su.custom == "11973102275"
