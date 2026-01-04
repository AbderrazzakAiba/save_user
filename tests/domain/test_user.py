def test_user_can_be_created_with_valid_names():
    from src.domain.user import User
    from src.domain.name import Name

    first_name = Name("Abderrazzak")
    last_name = Name("Aiba")

    user = User(first_name=first_name, last_name=last_name)

    assert user.first_name == first_name
    assert user.last_name == last_name
