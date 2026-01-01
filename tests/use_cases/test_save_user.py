from unittest.mock import Mock

from src.use_cases.save_user.use_case import SaveUserUseCase
from src.use_cases.save_user.command import CreateUserCommand


def test_save_user_success():
    # Arrange
    presenter = Mock()
    repository = Mock()

    use_case = SaveUserUseCase(repository, presenter)

    command = CreateUserCommand(
        first_name="Abderrazzak",
        last_name="Aiba"
    )

    # Act
    use_case.execute(command)

    # Assert
    presenter.present.assert_called_once()
