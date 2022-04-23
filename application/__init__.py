from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# The DB below will require the location (root for me) and password (just before @localhost if required)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/lotr_shop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


from application import routes

