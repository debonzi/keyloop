def test_user_password(registry):
    u = registry.User(email="debonzi@gmail.com")
    u.custom = "11973102275"
    u.password = "123123123a"
    u.save()

    su = registry.User.objects.get(  # pylint: disable=maybe-no-member
        {"_id": "debonzi@gmail.com"}
    )

    assert su.password != "123123123a"
    assert su.password_check("123123123a") is True
    assert su.custom == "11973102275"
