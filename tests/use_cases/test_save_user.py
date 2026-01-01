from unittest.mock import Mock

class SaveUserUseCase:
    def __init__(self, repository, presenter):
        self.presenter = presenter

    def execute(self, command):
        self.presenter.present(None)


class CreateUserCommand:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


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
