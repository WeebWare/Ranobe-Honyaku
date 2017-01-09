from functools import wraps

from flask import redirect, url_for, g


def login_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return wrapped


def anon_only(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if g.user is not None:
            return redirect(url_for("index"))
        return func(*args, **kwargs)
    return wrapped
