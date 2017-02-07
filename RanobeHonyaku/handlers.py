def error_404_not_found(e):
    return


def error_401_unauthorized(e):
    return


def error_500_server_error(e):
    return


def error_403_forbidden(e):
    return


handlers = {
    401: error_401_unauthorized,
    403: error_403_forbidden,
    404: error_404_not_found,
    500: error_500_server_error
}
