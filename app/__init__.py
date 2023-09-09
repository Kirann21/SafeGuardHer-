# from flask import Flask

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key_here'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use the appropriate database URI

# from app import routes


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config.Config')  # Use the Config class from config.py
db = SQLAlchemy(app)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes  # Import routes at the end to avoid circular import
