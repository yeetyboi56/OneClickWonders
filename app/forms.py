from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email address", validators=[InputRequired(), Length(4, 128), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = StringField("Email address", validators=[InputRequired(), Length(4, 128), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    password_confirm = PasswordField("Confirm Password", validators=[InputRequired(), Length(min=8),
                                                                     EqualTo("password", "Passwords must match.")])
    submit = SubmitField("Register")
