from src.use_cases.save_user.output_dto import OutputDTO
from src.use_cases.save_user.boundaries.presenter_interface import PresenterInterface


class SaveUserUseCase:
    def __init__(self, repository, presenter: PresenterInterface):
        self.repository = repository
        self.presenter = presenter

    def execute(self, command):
        if self._is_invalid(command):
            return self._present_failure("INVALID_NAME")

        if self._user_already_exists(command):
            return self._present_failure("USER_ALREADY_EXISTS")

        return self._present_success()

    # ---------- Private helpers ----------

    def _is_invalid(self, command):
        return (
            not self._is_valid_name(command.first_name)
            or not self._is_valid_name(command.last_name)
        )

    def _user_already_exists(self, command):
        return self.repository.exists(
            command.first_name,
            command.last_name
        )

    def _is_valid_name(self, name: str) -> bool:
        return name.isalpha()

    def _present_success(self):
        self.presenter.present(
            OutputDTO(success=True)
        )

    def _present_failure(self, error_code: str):
        self.presenter.present(
            OutputDTO(success=False, error=error_code)
        )
