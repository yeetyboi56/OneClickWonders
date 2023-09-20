import uuid
from dataclasses import asdict

from flask import Blueprint, render_template, session, redirect, url_for, current_app, flash
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from app.forms import RegisterForm
from app.models import User

register_route = Blueprint("register", __name__)


@register_route.route('/register/', methods=["GET", "POST"])
def register():
    if session.get("email"):
        return redirect(url_for("index.index"))

    form = RegisterForm()

    if form.validate_on_submit():
        if current_app.db.users.find_one({"email": form.email.data}):
            flash("There is already a user associated with that email")
            return render_template("register.html", title="Register", form=form)

        user = User(
            _id=uuid.uuid4().hex,
            email=form.email.data,
            password=pbkdf2_sha256.hash(form.password.data)
        )

        current_app.db.users.insert_one(asdict(user))

        flash("Successfully created an account")

        return redirect(url_for("login.login"))

    return render_template("register.html", title="Register", form=form)
