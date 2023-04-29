from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import UserMixin, LoginManager
from imports import database

app = Flask(__name__)
login_manager = LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2008@localhost/ash'

db = SQLAlchemy(app)

class user(db.Model , UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer , primary_key = True)
    password = db.Column(db.String(40) , nullable=False)
    email = db.Column(db.String(40) , unique=True , nullable = False)
    status = db.Column(db.String(10) , default='CLIENT')

    def __init__(self,username , password, email):
        self.username = username
        self.password = password
        self.email = email
    def __repr__(self):
        return f'<User: {self.id}'


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(user_id)