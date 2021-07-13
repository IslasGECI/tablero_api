from tablero.request_validator.validator import is_valid_user


class Request:
    def __init__(self, analista):
        self.args = {"analista": analista}


def test_is_valid_user():
    not_valid_request = Request("inspector")
    is_valid_analista = is_valid_user(not_valid_request)
    assert not is_valid_analista
    valid_request = Request("no_inspector")
    is_valid_analista = is_valid_user(valid_request)
    assert is_valid_analista
