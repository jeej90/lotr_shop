import login as login
from application import db, login_manager
from flask import session, redirect, url_for, abort
from datetime import datetime
from flask_login import UserMixin, current_user, login_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import update
# from sqlalchemy import declarative_base
# Base = declarative_base()
# class User(Base):


# Function to load a user for the login feature
@login_manager.user_loader
def load_user(registered_user_id):
    return RegisteredUser.query.get(int(registered_user_id))


# JeJe: added customer address relationship as one-to-one relationship
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    DOB = db.Column(db.DATE, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact_no = db.Column(db.String(11), nullable=False)
    address = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    customer_address = db.relationship('Address', backref='customer', uselist=False)
    registered_user = db.relationship('RegisteredUser', backref='customer', uselist=False)

    # method that prints our object as a string
    def __repr__(self):
        return f"Customer('{self.first_name} {self.last_name}', '{self.email}', '{self.contact_no}')"


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line1 = db.Column(db.String(50), nullable=False)
    address_line2 = db.Column(db.String(50), nullable=False)
    address_line3 = db.Column(db.String(50), nullable=True)
    county = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return f"{self.address_line1}, {self.address_line2}, {self.county}, {self.postcode}"


# JeJe: added unique=True for fields that need to be unique
# JeJe: added nullable as True for customer_id
# JeJe: added password attribute
class RegisteredUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.now)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=True)

    def __repr__(self):
        return f"Registered User({self.user_name}, {self.email})"


# JeJe: added product classes

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1500), nullable=False)
    # need to change full price from string to float so we can manipulate this
    full_price = db.Column(db.String(50), nullable=False)
    barcode = db.Column(db.String(200), unique=True, nullable=False)
    available_stock = db.Column(db.Integer)
    reserved_stock = db.Column(db.Integer)
    sold_stock = db.Column(db.Integer)
    # image = db.Column(db.String(200), nullable=False)
    # size_id = db.Column(db.Integer, db.ForeignKey('size.id'), nullable=True)
    colour_id = db.Column(db.Integer, db.ForeignKey('colour.id'), nullable=True)
    # stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=True)
    product_category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'), nullable=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=True)
    category = db.relationship('ProductCategory', backref='product')
    image = db.relationship('Image', backref='product')


    def __repr__(self):
        return f"Product({self.name}, {self.description}, {self.full_price})"


class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"{self.category}"


class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(50), nullable=False)


class Colour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colour = db.Column(db.String(50), nullable=False)


# class Stock(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     available_stock = db.Column(db.String(200), nullable=False)
#     reserved_stock = db.Column(db.Integer)
#     sold_stock = db.Column(db.Integer)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
#
#     def __repr__(self):
#         return f"Stock('{self.available_stock}', '{self.reserved_stock}', {self.full_price})"

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.name}"


class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=True)
    admin_staff = db.relationship('Staff', backref='staff')


class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    DOB = db.Column(db.DATE, nullable=True)
    job_title = db.Column(db.String(100), unique=True, nullable=False)
    start_date = db.Column(db.DATE, nullable=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    staff_address = db.relationship('Address', backref='staff', uselist=False)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.job_title}"

# @login.user_loader
# def load_admin(id):
#     return Administrator.query.get(id)


class MyModelView(ModelView):
    column_display_pk = True  # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    def is_accessible(self):
        # return current_user.is_authinticated
        if "logged_in" in session:
            return True
        else:
            # abort(403)
            return redirect(url_for('admin_login'))


class MyAdminView(AdminIndexView):
    def is_accessible(self):
        # return current_user.is_authinticated
        if "logged_in" in session:
            return True
        else:
            # abort(403)
            return redirect(url_for('admin_login'))


# Mya and Alice order confirmation - creating following classes: order_status, customerorder

#creating customer order table
class JsonEncodedDict(db.TypeDecorator):
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)
    def process_result_value(selfself, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice = db.Column(db.String(20), unique=True, nullable=False)
    # should the status be called order_status_id and be a foreign key with the order_status_id from the order_status table??
    status = db.Column(db.String(30), default='Pending', nullable=False)
    # should the customer_id be a foreign key with the customer_id from the customer table??
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=True)
    customer = db.relationship('Customer', backref='customerorder', uselist=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    orders = db.Column(JsonEncodedDict)


    def __repr__(self):
        return'<CustomerOrder %r>' % self.invoice

class OrderStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_status = db.Column(db.String(30), unique=True, nullable=False)


db.create_all()