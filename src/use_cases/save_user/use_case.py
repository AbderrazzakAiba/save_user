from src.use_cases.save_user.output_dto import OutputDTO
from src.use_cases.save_user.boundaries.presenter_interface import PresenterInterface


class SaveUserUseCase:
    def __init__(self, repository, presenter: PresenterInterface):
        self.repository = repository
        self.presenter = presenter

    def execute(self, command):
        if self._user_already_exists(command):
            self._present_user_already_exists()
        else:
            self._present_user_created()

    def _user_already_exists(self, command):
        return self.repository.exists(
            command.first_name,
            command.last_name
        )

    def _present_user_already_exists(self):
        self.presenter.present(OutputDTO(success=False))

    def _present_user_created(self):
        self.presenter.present(OutputDTO(success=True))
