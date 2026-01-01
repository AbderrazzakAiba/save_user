from unittest.mock import Mock

from src.use_cases.save_user.use_case import SaveUserUseCase
from src.use_cases.save_user.command import CreateUserCommand
from src.use_cases.save_user.output_dto import OutputDTO


def test_save_user_success():
    presenter = Mock()
    repository = Mock()
    repository.exists.return_value = False

    use_case = SaveUserUseCase(repository, presenter)

    command = CreateUserCommand(
        first_name="Abderrazzak",
        last_name="Aiba"
    )

    use_case.execute(command)

    presenter.present.assert_called_once_with(
        OutputDTO(success=True)
    )


def test_save_user_when_user_already_exists():
    presenter = Mock()
    repository = Mock()
    repository.exists.return_value = True

    use_case = SaveUserUseCase(repository, presenter)

    command = CreateUserCommand(
        first_name="Abderrazzak",
        last_name="Aiba"
    )

    use_case.execute(command)

    presenter.present.assert_called_once_with(
        OutputDTO(success=False)
    )

def test_save_user_with_invalid_name_should_fail():
    presenter = Mock()
    repository = Mock()
    repository.exists.return_value = False

    use_case = SaveUserUseCase(repository, presenter)

    command = CreateUserCommand(
        first_name="Abd3r",
        last_name="Aiba"
    )

    use_case.execute(command)

    presenter.present.assert_called_once_with(
        OutputDTO(success=False)
    )

