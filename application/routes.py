from flask import render_template, request, redirect, url_for
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from application.models import RegisteredUser


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="Lord of the Rings Shop")


@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    #
    # if request.method == 'POST':
    #     user_name = form.user_name.data
    #     email = form.email.data
    #     password = form.password.data
    #
    #     if len(user_name) == 0 or len(email) == 0 or len(password) == 0:
    #         error = "Please supply all required fields"
    #     else:
    #         registered_user = RegisteredUser(user_name=user_name, email=email, password=password)
    #         db.session.add(registered_user)
    #         db.session.commit()
    #         return 'Registration successful! Welcome to Middle Earth :)'

    return render_template("register.html", title="Sign up", form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", title="Sign in")
