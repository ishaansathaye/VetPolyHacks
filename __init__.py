from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#from Project.Ebay import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '194e8b78e4d7cfd736b218d4'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "loginPage"
login_manager.login_message_category = "info"
from Scrape import routes
