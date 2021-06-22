from tablero.request_validator.validator import is_valid_user


class Request:
    def __init__(self):
        self.args = {"analista": "inspector"}


def test_is_valid_user():
    request = Request()
    obtained_is_valid_analista = is_valid_user(request)
    expected_is_valid_analista = False
    assert obtained_is_valid_analista == expected_is_valid_analista
