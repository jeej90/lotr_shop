import secrets

from flask import render_template, flash, redirect, url_for, request, session, current_app
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm, AdminLogin, CustomerDetails
from application.models import RegisteredUser, Product, Image, Administrator, Staff, Purchase, Customer, Address
from flask_login import login_user, current_user, logout_user, login_required
from flask_admin import Admin


@app.route('/')
@app.route('/home')
def home():
    products = Product.query.all()
    return render_template("home.html", title="Lord of the Rings Emporium", products=products)

@app.route('/home2')
def home2():
    return render_template("home2.html", title="Lord of the Rings Emporium")


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


@app.route("/adminlogin", methods=['GET', 'POST'])
def admin_login():
    # session["logged_in"] = True
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = AdminLogin()
    if form.validate_on_submit():
        admin = Administrator.query.filter_by(user_name=form.user_name.data).first()
        password = Administrator.query.filter_by(password=form.password.data).first()
        if admin and password:
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin'))
        else:
            flash('Login unsuccessful. Please check username and password')
    return render_template('admin_login.html', title='Admin login', form=form)


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/logout")
def logout():
    logout_user()
    # session.clear()
    return redirect(url_for('home'))


@app.route("/adminlogout")
def admin_logout():
    session["logged_in"] = True
    session.clear()
    return redirect(url_for('home'))

# Dynamic route that creates a page for each product: it filters by  id and returns desired rows of data from the db
# The route points to the template HTML product page
#@app.route('/')
@app.route('/product/<int:id>')
def product(id):
    # products = Product.query.all()
    products = Product.query.filter_by(id=id)
    for product in products:
        print(product.name, product.description, product.full_price, product.image_id)
        image = Image.query.filter_by(id=product.image_id)
        for i in image:
            print(i.name)
        print(product.name, product.description, product.full_price, product.available_stock)
    return render_template("product.html",
                           image_name=i.name,
                           name=product.name,
                           description=product.description,
                           price=product.full_price,
                           available_stock=product.available_stock,
                           product_id=id)


# def cart_items(item1, item2):
#     print(type(item1))
#     print(type(item2))
#     if isinstance(item1, list) and isinstance(item2, list):
#         return item1 + item2
#     if isinstance(item1, dict) and isinstance(item2, dict):
#         return dict(list(item1.item() + item2.item()))


@app.route("/add", methods=['POST'])
def add_to_cart():
    try:
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
        product = Product.query.filter_by(id=product_id).first()

        if product_id and quantity and request.method == "POST":
            CartItem = {product_id: {'name': product.name, 'price': float(product.full_price), 'quantity': quantity}}
            if 'Cart' in session:
                cart = session['Cart']
                print(cart)
                if product_id in session['Cart']:
                    for key, item in session['Cart']:
                        if int(key) == int(product_id):
                            session.modified = True
                            item['quantity'] += 1
                else:
                    # session['Cart'] = cart_items(session['Cart'], CartItem)
                    current_cart = session['Cart']
                    current_cart.update(CartItem)
                    session['Cart'] = current_cart
                    return redirect('cart.html')
            else:
                session['Cart'] = CartItem
                flash(f'Item added to your shopping cart!')
                return render_template('cart.html')

    except Exception as e:
        print(e)
    finally:
        return render_template("cart.html")


@app.route('/cart')
def get_cart():
    if 'Cart' not in session or len(session['Cart']) <= 0:
        return redirect(url_for('home'))
    # subtotal = 0
    grand_total = 0
    for key, product in session['Cart'].items():
        grand_total += float(product['price']) * int(product['quantity'])
    return render_template('cart.html', grand_total=grand_total)


# @app.route("/cart", methods=['GET', 'POST'])
# def cart():
#     return render_template("cart.html")


@app.route('/updatecart/<int:code>', methods=['POST'])
def update_cart(code):
    if 'Cart' not in session or len(session['Cart']) <= 0:
        return redirect(url_for('home'))
    if request.method == "POST":
        quantity = request.form.get('quantity')
        try:
            session.modified = True
            for key, item in session['Cart'].items():
                if int(key) == code:
                    item['quantity'] = quantity
                    flash('Item is updated!')
                    return redirect(url_for('get_cart'))
        except Exception as e:
            print(e)
            return redirect(url_for('get_cart'))


@app.route('/deleteitem/<int:id>')
def delete_item(id):
    if 'Cart' not in session or len(session['Cart']) <= 0:
        return redirect(url_for('home'))
    try:
        session.modified = True
        for key, item in session['Cart'].items():
            if int(key) == id:
                session['Cart'].pop(key, None)
                return redirect(url_for('get_cart'))
    except Exception as e:
        print(e)
        return redirect(url_for('get_cart'))


@app.route('/clearcart')
def clear_cart():
    try:
        session.pop('Cart', None)
        flash('Your cart is empty.')
        return redirect(url_for('get_cart'))
    except Exception as e:
        print(e)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if current_user.is_authenticated:
        customer_id = current_user.id
    form = CustomerDetails()
    if form.validate_on_submit():
        customer_info = Customer(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
        customer_address = Address(address_line1=form.address1.data, address_line2=form.address2.data, address_line3=form.address3.data, county=form.address4.data, postcode=form.address5.data,)
        db.session.add(customer_info)
        db.session.add(customer_address)
        db.session.commit()
        flash("Thank you")
        return redirect(url_for('order_confirmed'))
    return render_template('checkout.html', form=form)

@app.route('/confirmed')
def order_confirmed():
    session.pop('Cart', default=None)
    return render_template('confirmation.html')


# @app.route('/purchaseupdate')
# def update_purchase():
#     if current_user.is_authenticated:
#         customer_id = current_user.id
#
#
#
#
# # Mya and Alice - order confirmation
#
# # created a route to get the order details and input into order table in the database
# @app.route('/getorder')
# @login_required
# def get_order():
#     if current_user.is_authenticated:
#         customer_id = current_user.id
#         #can we get rid of invoice? Use the order_id as the invoice number
#         invoice = Purchase.query.filter_by(id=)
#         try:
#             # possibly remove invoice and replace with order_id
#             order = Order(invoice=invoice, customer_id=customer_id, orders=session
#                                   ['Shoppingcart'])
#             db.session.add(order)
#             db.session.commit
#             session.pop('Shoppingcart')
#             flash('Your order has been sent successfully', 'success')
#             return redirect(url_for('home'))
#         except Exception as e:
#             print(e)
#             flash('Some thing went wrong while getting your order details', 'danger')
#             return redirect(url_for('getCart'))
#
#
# @app.route('/orders/<invoice>')
# @login_required
# def orders(invoice):
#     if current_user.is_authenticated:
#         orderTotal = 0
#         customer_id = current_user.id
#         customer = Register.query.filter_by(id=customer_id).first()
#         orders = CustomerOrder.query.filter_by(customer_id=customer_id).first()
#         for _key, product in orders.orders.items():
#             orderTotal += float(product['price']) + int(product['quantity'])
#     else:
#         return redirect(url_for('customerLogin'))
#     return render_template('customer/login.html', invoice=invoice, orderTotal=orderTotal, customer=customer, orders=orders)


@app.route('/')
@app.route('/clothes')
def clothes():
    products = Product.query.filter_by(product_category_id=1)
    for product in products:
        print(product.image)
    return render_template("clothes.html", title="Clothes", products=products, product_image=product.image)


# this route points to the keyrings product page, which displays all the keyring products in the database
@app.route('/keyrings')
def keyrings_and_badges():
    products = Product.query.filter_by(product_category_id=3)
    for product in products:
        print(product.image)
    return render_template("keyrings_and_badges.html", title="Keyrings & Badges", products=products, product_image=product.image)


# this route points to the collectibles product page, which displays all the collectibles products in the database
@app.route('/collectibles')
def collectibles():
    products = Product.query.filter_by(product_category_id=4)
    for product in products:
        print(product.image)
    return render_template("collectibles.html", title="Collectibles", products=products, product_image=product.image)


# this route points to the games product page, which displays all the games products in the database
@app.route('/games')
def games():
    products = Product.query.filter_by(product_category_id=2)
    for product in products:
        print(product.image)
    return render_template("games.html", title="Games", products=products, product_image=product.image)


# This route points to a page which displays all products in the database
@app.route('/')
@app.route('/products')
def products():
    products = Product.query.filter_by(product_category_id=2)
    for product in products:
        print(product.image)
    return render_template("products.html", title="Products", products=products, product_image=product.image)

#this route is for displaying multiple images, do not use unless we decide to use multiple images
# @app.route('/chess')
# def chess_deluxe():
#     products = Product.query.filter_by(name='Lord of the Rings Collectible Chess Set - Officially Licensed Film Set Movie Gifts')
#     return render_template("product_chess_deluxe.html", title="Chess Set", products=products)


@app.errorhandler(404)
def invalid_route(e):
    return render_template('error404.html')
