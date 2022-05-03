from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from application.models import RegisteredUser, Customer
from flask_login import current_user


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
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AdminLogin(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class CustomerDetails(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=100)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=100)])
    address1 = StringField('Address Line 1', validators=[DataRequired(), Length(min=2, max=100)])
    address2 = StringField('Address Line 2')
    address3 = StringField('Address Line 3')
    address4 = StringField('County', validators=[DataRequired(), Length(min=2, max=100)])
    address5 = StringField('Postcode', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Confirm Order')


class UpdateAccount(FlaskForm):
    user_name = StringField('User name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=100)])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    address1 = StringField('Address Line 1')
    address2 = StringField('Address Line 2')
    address3 = StringField('Address Line 3')
    address4 = StringField('County')
    address5 = StringField('Postcode')
    submit = SubmitField('Update')

    def validate_user_name(self, user_name):
        if user_name.data != current_user.user_name:
            user_found = RegisteredUser.query.filter_by(user_name=user_name.data).first()
            if user_found:
                raise ValidationError('This username is already taken. Please choose another.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user_found = RegisteredUser.query.filter_by(email=email.data).first()
            if user_found:
                raise ValidationError('There is already an account with this email.')