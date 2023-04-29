from flask import Flask , render_template , request , url_for,redirect
from imports import routes
from flask_login import login_user , login_required , LoginManager , UserMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2008@localhost/ash'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'thisismylittlesecret'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class user(db.Model , UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))
    email = db.Column(db.String(40))
    status = db.Column(db.String(10), default='CLIENT')

    name = db.Column(db.String(255), nullable=False)
    about = db.Column(db.Text(255), nullable=False)
    date = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text(255), nullable=False)
    price = db.Column(db.Integer , nullable = False)

    def __repr__(self):
        return f'<user {self.email}>'

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


@app.route(routes.show , methods = ['GET', 'POST'])
def mainPage():
    return render_template('index.html')


@app.route(routes.moder , methods = ['POST' , 'GET'])
@login_required
def modPage():
    return render_template('text_mer.html')

@app.route(f'{routes.form}/id' , methods = ['GET' ,'POST'])
@login_required
def formPage():
    if request.method == 'POST':
        username = request.form.get('username')
        use = user.query.filter_by(username=username).first()
        name = request.form.get('name')
        about = request.form.get('about')
        date = request.form.get('date')
        address = request.form.get('address')
        price = request.form.get('price')

        place = user(username=use.username , password=use.password ,
                     email=use.email , name = name , about=about ,
                     date=date , address=address , price=price)
        db.session.add(place)
        db.session.commit()


    return render_template('form_mer.html')


@app.route(routes.reg , methods = ['GET' , 'POST'])
def regPage():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get("email")

        User = user(username=username,password=password,email=email)
        db.session.add(User)
        db.session.commit()

        return redirect(location=url_for('login_post'))


    return render_template("reg.html")


@app.route(routes.main, methods=['POST','GET'])
def login_post():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        User =user.query.filter_by(email=email).first()
        if User:
            if User.password == password:
                login_user(User)

                return redirect(location=url_for('mainPage'))

    return render_template('login.html')


if __name__ == '__main__':
    app.run()