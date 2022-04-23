from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from application.models import RegisteredUser


# JeJe: added reg & login forms
class RegistrationForm(FlaskForm):
    user_name = StringField('User name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


    def validate_user_name(self, user_name):
        user_found = RegisteredUser.query.filter_by(user_name=user_name.data).first()
        if user_found:
            raise ValidationError('This username is already taken. Please choose another.')

    def validate_email(self, email):
        user_found = RegisteredUser.query.filter_by(email=email.data).first()
        if user_found:
            raise ValidationError('There is already an account with this email.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
