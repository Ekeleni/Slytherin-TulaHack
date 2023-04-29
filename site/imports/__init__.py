from flask import Flask
from imports import routes
from imports import database
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2008@localhost/ash'

db = SQLAlchemy(app)
login_manager = LoginManager(app)