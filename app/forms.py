# /app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models.user import User
import bcrypt

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.get_user_by_email(field.data):
            raise ValidationError('Email Already Taken')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class InfoForm(FlaskForm):
    data = StringField("Enter your information", validators=[DataRequired()])
    submit = SubmitField("Submit")

class UserInfoForm(FlaskForm):
    name = StringField("Nom", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Soumettre")