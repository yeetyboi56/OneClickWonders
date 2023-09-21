import functools

from flask import session, redirect, url_for, current_app, flash


def login_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if "email" not in session or "user_id" not in session:
            session.clear()
            flash("You need to be logged in to use this page")
            return redirect(url_for('login.login'))

        user_data = current_app.db.users.find_one({'email': session.get("email"), '_id': session.get("user_id")})

        if not user_data:
            session.clear()
            flash("You need to be logged in to use this page")
            return redirect(url_for('login.login'))

        return f(*args, **kwargs)

    return wrapper
