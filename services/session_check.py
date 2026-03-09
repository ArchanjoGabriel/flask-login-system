from flask import session, redirect, url_for
from functools import wraps

def session_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect(url_for("login_signin.login_page"))
        return func(*args, *kwargs)
    return wrapper