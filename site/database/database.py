from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2008@localhost/ash'

db = SQLAlchemy(app)

class user(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))
    email = db.Column(db.String(40))
    status = db.Column(db.String(10) , default='CLIENT')

    def __init__(self,username , password, email):
        self.username = username
        self.password = password
        self.email = email