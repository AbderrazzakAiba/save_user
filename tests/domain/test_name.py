import pytest


def test_name_cannot_be_empty():
    from src.domain.name import Name, InvalidNameError

    with pytest.raises(InvalidNameError):
        Name("")


def test_name_cannot_contain_digits():
    from src.domain.name import Name, InvalidNameError

    with pytest.raises(InvalidNameError):
        Name("Ali1")