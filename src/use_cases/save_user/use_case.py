from src.use_cases.save_user.output_dto import OutputDTO
from src.use_cases.save_user.boundaries.presenter_interface import PresenterInterface
from src.domain.name import Name, InvalidNameError
from src.domain.user import User


class SaveUserUseCase:
    def __init__(self, repository, presenter: PresenterInterface):
        self.repository = repository
        self.presenter = presenter

    def execute(self, command):
        try:
            first_name = Name(command.first_name)
            last_name = Name(command.last_name)
        except InvalidNameError:
            return self._present_failure("INVALID_NAME")

        if self.repository.exists(first_name.value, last_name.value):
            return self._present_failure("USER_ALREADY_EXISTS")

        user = User(first_name=first_name, last_name=last_name)

        self.repository.save(user)

        return self._present_success()

    def _present_success(self):
        self.presenter.present(OutputDTO(success=True))

    def _present_failure(self, error_code: str):
        self.presenter.present(OutputDTO(success=False, error=error_code))
