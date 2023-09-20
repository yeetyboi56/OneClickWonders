from flask import Blueprint, render_template, flash, redirect, url_for, session, current_app
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from app.forms import LoginForm
from app.models import User

login_route = Blueprint("login", __name__)


# email: test@email.com
# password: 123456789


@login_route.route("/login/", methods=["GET", "POST"])
def login():
    if session.get("email"):
        return redirect(url_for("index.index"))

    form = LoginForm()

    if form.validate_on_submit():
        user_data = current_app.db.users.find_one({"email": form.email.data})

        if not user_data:
            flash("Login credentials are not correct")
            return redirect(url_for("login.login"))

        user = User(**user_data)

        if user and pbkdf2_sha256.verify(form.password.data, user.password):
            session["user_id"] = user._id
            session["email"] = user.email

            return redirect(url_for("index.index"))

        flash("Login credentials are not correct")

    return render_template("login.html", title="Login", form=form)


@login_route.route("/logout/")
def logout():
    session.clear()
    flash("Successfully logged out")
    return redirect(url_for(".login"))
