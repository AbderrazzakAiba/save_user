


def test_name_cannot_be_empty():
    from src.domain.name import Name, InvalidNameError

    with pytest.raises(InvalidNameError):
        Name("")
