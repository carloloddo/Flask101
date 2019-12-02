from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.settings.config import SECRET_KEY, SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
login = LoginManager(app)

from app.controllers.main import main
from app.controllers.users import users

app.register_blueprint(main)
app.register_blueprint(users)