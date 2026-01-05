class InMemoryUserRepository:
    def __init__(self):
        self._users = []

    def exists(self, first_name: str, last_name: str) -> bool:
        return any(
            user.first_name.value == first_name
            and user.last_name.value == last_name
            for user in self._users
        )

    def save(self, user) -> None:
        self._users.append(user)
