from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):

    @abstractmethod
    def exists(self, first_name: str, last_name: str) -> bool:
        pass
