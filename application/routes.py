from flask import render_template, flash, redirect, url_for, request
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
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = RegisteredUser(user_name=form.user_name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account successfully created. Welcome to Middle Earth!')
        return redirect(url_for('login'))

    return render_template("register.html", title="Sign up", form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title="Sign in", form=form)
