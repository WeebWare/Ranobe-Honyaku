from flask import render_template


def error_404_not_found(e):
    return render_template("error.html", error=e)


def error_401_unauthorized(e):
    return render_template("error.html", error=e)


def error_500_server_error(e):
    return render_template("error.html", error=e)


def error_403_forbidden(e):
    return render_template("error.html", error=e)


handlers = {
    401: error_401_unauthorized,
    403: error_403_forbidden,
    404: error_404_not_found,
    500: error_500_server_error
}
