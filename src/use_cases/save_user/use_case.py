from src.use_cases.save_user.output_dto import OutputDTO
from src.use_cases.save_user.boundaries.presenter_interface import PresenterInterface


class SaveUserUseCase:
    def __init__(self, repository, presenter: PresenterInterface):
        self.repository = repository
        self.presenter = presenter

    def execute(self, command):
        if not self._is_valid_name(command.first_name) or not self._is_valid_name(command.last_name):
            self.presenter.present(OutputDTO(success=False))
            return

        if self.repository.exists(command.first_name, command.last_name):
            self.presenter.present(OutputDTO(success=False))
            return

        self.presenter.present(OutputDTO(success=True))

    def _is_valid_name(self, name: str) -> bool:
        return name.isalpha()
