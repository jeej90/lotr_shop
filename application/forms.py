from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField


# JeJe: added reg form
class RegistrationForm(FlaskForm):
    user_name = StringField('User name')
    email = StringField('Email')
    password = StringField('Password')
    submit = SubmitField('Register')


