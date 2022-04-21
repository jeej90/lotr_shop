from application import db

class Customer(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    DOB = db.Column(db.DATE, nullable=True)
    email = db.Column(db.String(100), nullable=False)
    contact_no = db.Column(db.String(11), nullable=False)
    address = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    registered_user = db.relationship('RegisteredUser', backref='customer')

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line1 = db.Column(db.String(50), nullable=False)
    address_line2 = db.Column(db.String(50), nullable=False)
    address_line3 = db.Column(db.String(50), nullable=True)
    county = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(8), nullable=False)

class RegisteredUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_joined = db.Column(db.DATETIME, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

