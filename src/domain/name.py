class InvalidNameError(Exception):
    pass


class Name:
    def __init__(self, value: str):
        self._validate(value)
        self.value = value

    def _validate(self, value: str):
        if not value:
            raise InvalidNameError()

        if not value.isalpha():
            raise InvalidNameError()