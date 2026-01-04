class InvalidNameError(Exception):
    pass


class Name:
    def __init__(self, value: str):
        if value == "":
            raise InvalidNameError()

        if not value.isalpha():
            raise InvalidNameError()

        self.value = value
