from flask import render_template, flash, redirect, url_for, request
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from application.models import RegisteredUser
from flask_login import login_user


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="Lord of the Rings Emporium")


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
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = RegisteredUser.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password')
    return render_template('login.html', title='Login', form=form)
