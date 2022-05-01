from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# The DB below will require the location (root for me) and password (just before @localhost if required)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/lotr_shop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_login import LoginManager
login_manager = LoginManager(app)

from flask_admin import Admin
from application.models import Administrator, MyModelView, MyAdminView, Product, Image, RegisteredUser, Customer, Address, ProductCategory, Staff, Purchase
# from flask_admin.contrib.sqla import ModelView

admin = Admin(app, index_view=MyAdminView())

admin.add_view(MyModelView(Product, db.session))
admin.add_view(MyModelView(ProductCategory, db.session))
admin.add_view(MyModelView(Image, db.session))
admin.add_view(MyModelView(RegisteredUser, db.session))
admin.add_view(MyModelView(Customer, db.session))
admin.add_view(MyModelView(Address, db.session))
admin.add_view(MyModelView(Administrator, db.session))
admin.add_view(MyModelView(Staff, db.session))
admin.add_view(MyModelView(Purchase, db.session))


from application import routes
