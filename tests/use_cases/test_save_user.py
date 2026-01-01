
from unittest.mock import Mock


def test_save_user_success():
    presenter = Mock()
    repository = Mock()

    from src.use_cases.save_user.use_case import SaveUserUseCase
    from src.use_cases.save_user.command import CreateUserCommand

    use_case = SaveUserUseCase(repository, presenter)

    command = CreateUserCommand(
        first_name="Abderrazzak",
        last_name="Aiba"
    )

    use_case.execute(command)

    presenter.present.assert_called_once()