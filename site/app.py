from flask import Flask , render_template , request , url_for,redirect
from imports import routes
from imports import database
from flask_login import login_user , login_required
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
@login_required
def modPage():
    return render_template('text_mer.html')

@app.route(routes.form , methods = ['GET' ,'POST'])
@login_required
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



@app.route(routes.login, methods=['POST','GET'])
def login_post():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user =database.user.query.filter_by(email=email).first
        if database.user.password == password:
            login_user(user)
            return redirect(url_for('/'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run()