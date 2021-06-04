def validate_request(request):
    is_valid_request = is_valid_user(request)
    return is_valid_request


def is_valid_user(request):
    is_valid_analista = request.args["analista"] != "inspector"
    return is_valid_analista
