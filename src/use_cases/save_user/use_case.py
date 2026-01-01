from src.use_cases.save_user.output_dto import OutputDTO
from src.use_cases.save_user.boundaries.presenter_interface import PresenterInterface


class SaveUserUseCase:
    def __init__(self, repository, presenter: PresenterInterface):
        self.repository = repository
        self.presenter = presenter

    def execute(self, command):
        self.presenter.present(OutputDTO(success=True))
