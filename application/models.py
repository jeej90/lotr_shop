from application import db, login_manager
from datetime import datetime
from flask_login import UserMixin
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
        return f"Customer('{self.first_name}', '{self.last_name}', '{self.email}', '{self.contact_no}')"


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line1 = db.Column(db.String(50), nullable=False)
    address_line2 = db.Column(db.String(50), nullable=False)
    address_line3 = db.Column(db.String(50), nullable=True)
    county = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return f"Address('{self.address_line1}', '{self.address_line2}', '{self.address_line3}', '{self.county}', '{self.postcode}')"


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
        return f"Registered User('{self.user_name}', '{self.email}')"


# JeJe: added product classes
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    # need to change full price from string to float so we can manipulate this
    full_price = db.Column(db.String(50), nullable=False)
    barcode = db.Column(db.String(200), unique=True, nullable=False)
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'), nullable=True)
    colour_id = db.Column(db.Integer, db.ForeignKey('colour.id'), nullable=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=True)
    product_category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'), nullable=True)

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.full_price})"


class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)


class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(50), nullable=False)


class Colour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colour = db.Column(db.String(50), nullable=False)


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    available_stock = db.Column(db.String(200), nullable=False)
    reserved_stock = db.Column(db.Integer)
    sold_stock = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)

    def __repr__(self):
        return f"Stock('{self.available_stock}', '{self.reserved_stock}', {self.full_price})"

