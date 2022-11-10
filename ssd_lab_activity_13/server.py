from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, login_manager, login_user, logout_user, login_required, UserMixin)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'new_secret_key'

db = SQLAlchemy(app)
login_manager = LoginManager()

login_manager.init_app(app)

class User(UserMixin, db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(name)

def connectNow():
    with app.app_context():
        db.create_all()

connectNow()

@app.route('/user/signin', methods = ['POST'])
def signin():
    if(request.method=='POST'):
        req = request.get_json()
        name = req['name']
        email = req['email']
        password = req['password']
        check_user = User.query.filter_by(name=name).first()
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user)
                return "log in successful!"
            else:
                return "Incorrect password!"
        else:
            return "User not found!"

@app.route('/user/signup', methods = ['POST'])
def signup():
    if(request.method=='POST'):
        req = request.get_json()
        name = req['name']
        email = req['email']
        password = req['password']
        obj = User(name=name, email=email, password=password)
        db.session.add(obj)
        db.session.commit()
        return "You have signed in successfully!"
    else :
        return "Sign up not successful!"

@app.route('/user/signout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route("/hello")
def hello_reply():
    return "Hello World!!"

if "__main__" == __name__ :
    app.run(host="127.0.0.1", port="5000", debug=True)