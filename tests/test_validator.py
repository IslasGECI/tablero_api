from tablero.request_validator.validator import is_valid_user


class Request:
    def __init__(self):
        self.args = {"analista": "inspector"}


def test_is_valid_user():
    request = Request()
    is_valid_analista = is_valid_user(request)
    assert not is_valid_analista
