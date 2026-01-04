def test_user_repository_has_exists_method():
    from src.use_cases.save_user.boundaries.user_repository_interface import (
        UserRepositoryInterface
    )

    assert hasattr(UserRepositoryInterface, "exists")
