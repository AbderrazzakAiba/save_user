def test_inmemory_repository_saves_user_and_detects_existence():
    from src.infrastructure.repositories.inmemory_user_repository import (
        InMemoryUserRepository
    )
    from src.domain.name import Name
    from src.domain.user import User

    repo = InMemoryUserRepository()

    user = User(
        first_name=Name("Abderrazzak"),
        last_name=Name("Aiba")
    )

    assert repo.exists("Abderrazzak", "Aiba") is False

    repo.save(user)

    assert repo.exists("Abderrazzak", "Aiba") is True
