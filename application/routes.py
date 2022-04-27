from flask import render_template, flash, redirect, url_for, request
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from application.models import RegisteredUser, Product
from flask_login import login_user, current_user, logout_user



@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="Lord of the Rings Emporium")


@app.route('/')
@app.route('/about')
def about():
    return render_template("about.html", title="FAQ")


@app.route('/')
@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact Us")


@app.route('/')
@app.route('/faq')
def faq():
    return render_template("faq.html", title="FAQ")


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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


# Dynamic route that creates a page for each product: it filters by  id and returns desired rows of data from the db
# The route points to the template HTML product page
@app.route('/')
@app.route('/product/<int:id>')
def product(id):
    # products = Product.query.all()
    products = Product.query.filter_by(id=id)
    # images = Image.query.filter_by(name=products)
    for product in products:
        print(product.name, product.description, product.full_price)
    return render_template("product.html",
                           name=product.name,
                           description=product.description,
                           price=product.full_price,
                           id=product)

# (in for loop?) and image in images
# (in return?)                            image=image.name,

# This route points to a product category page, it queries and filters results based on category id
@app.route('/')
@app.route('/clothes')
def clothes():
    products = Product.query.filter_by(product_category_id=1)
    return render_template("clothes.html", title="Clothes", products=products)


# this route points to the keyrings product page, which displays all the keyring products in the database
@app.route('/keyrings')
def keyrings_and_badges():
    products = Product.query.filter_by(product_category_id=3)
    return render_template("keyrings_and_badges.html", title="Keyrings & Badges", products=products)


# this route points to the collectibles product page, which displays all the collectibles products in the database
@app.route('/collectibles')
def collectibles():
    products = Product.query.filter_by(product_category_id=3)
    return render_template("collectibles.html", title="Collectibles", products=products)


# this route points to the games product page, which displays all the games products in the database
@app.route('/games')
def games():
    products = Product.query.filter_by(product_category_id=2)
    return render_template("games.html", title="Games", products=products)


# This route points to a page which displays all products in the database
@app.route('/')
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template("products.html", title="Products", products=products)

#this route is for displaying multiple images, do not use unless we decide to use multiple images
# @app.route('/chess')
# def chess_deluxe():
#     products = Product.query.filter_by(name='Lord of the Rings Collectible Chess Set - Officially Licensed Film Set Movie Gifts')
#     return render_template("product_chess_deluxe.html", title="Chess Set", products=products)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.errorhandler(404)
def invalid_route(e):
    return render_template('error404.html')
