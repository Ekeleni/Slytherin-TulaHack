from flask import Flask , render_template , request , url_for,redirect
from routes import *
from database import database
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2008@localhost/ash'

db = SQLAlchemy(app)

@app.route(routes.main , methods = ['GET', 'POST'])
def mainPage():
    if request.method == 'POST': #not working while
        redirect(url_for('/mod'))
    return render_template("index.html")

@app.route(routes.moder , methods = ['POST' , 'GET'])
def modPage():
    return render_template('text_mer.html')

@app.route(routes.form , methods = ['GET' ,'POST'])
def formPage():
    return render_template('form_mer.html')

@app.route(routes.reg , methods = ['GET' , 'POST'])
def regPage():
    if request.method == 'POST':
        username = request.form.get('nick')
        password = request.form.get('passwd')
        email = request.form.get("email")

        User = database.user(username , password , email)
        db.session.add(User)
        db.session.commit()

    return render_template("reg.html")


if __name__ == '__main__':
    app.run()