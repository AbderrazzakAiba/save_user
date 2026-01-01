from abc import ABC, abstractmethod
from src.use_cases.save_user.output_dto import OutputDTO


class PresenterInterface(ABC):

    @abstractmethod
    def present(self, output: OutputDTO) -> None:
        pass
