import os
from flask_migrate import Migrate

import email_validator
from flask import Flask, abort, render_template
from flask_bootstrap import Bootstrap
# from flask. import Moment
from flask_wtf import FlaskForm
from wtforms import (BooleanField, FileField, IntegerField, MultipleFileField,
                     PasswordField, StringField, SubmitField, TextAreaField,
                     validators)
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)

SECRET_KEY = os.urandom(32)

import requests
from flask import (Blueprint, flash, redirect, render_template, request,
                   send_from_directory, session, url_for)
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bootstrap = Bootstrap(app)
#moment = Moment(app)
app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# login_manager = LoginManager()
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'
# login_manager.init_app(app)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

migrate = Migrate(app, db)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    user_agent = request.headers.get('User-Agent')
    if form.validate_on_submit():
        
        #######TODO: Insert function to check the token from fakeapi = if true redirect to search else login page with error
        ###if old_name is not None and old_name != form.name.data:
            ###flash('Looks like you have changed your name!')
        user = User.query.filter_by(username=form.username.data).first()
        session['usr_name'] = form.username.data
        return redirect(url_for('search'))
    return render_template('login.html', title='login',form=form)


@app.route('/user/<name>/<comments>')
def user(name,comments):
    return render_template('user.html', name=name,comments=comments)

@app.route('/search', methods=['GET', 'POST'])
def search():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    #form = LoginForm()
    usr_name = session.get('usr_name')
    url = "https://fakestoreapi.com/auth/login"
    req_body = {"username": "mor_2314","password": "83r5^"}
    resp = requests.post(url, data = req_body)
    #abort(404)
    return render_template('search.html', title='search')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


def home(type):
  #mongo.db.items.find_one_or_404({'Type': type.title()})  # just to return 404 error if there is not a single item with that thing
  #items = mongo.db.items.find({'Type': type.title()})
  global itemType
  itemType = type  # so that same type of items are getched in filter results
  #brands = ret_brands(type)
  #categories = ret_categories('Men')
  #types = mongo.db.items.distinct('Type')
  return render_template('home.html')#, items=items, brands=brands, categories=categories, itemType=type.title(), types=types)



@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
        form = RequestResetForm()
        response_API = requests.get('https://www.askpython.com/')
        response_API.status_code
        return render_template('reset_request.html', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if user is None:
        user = User(username=form.name.data)
        db.session.add(user)
        db.session.commit()
        session['known'] = False
    else:
        session['known'] = True
    session['name'] = form.name.data
    return render_template('register.html', title='register', form=form)


class LoginForm(FlaskForm):
    username = StringField('User', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Request Reset Password')

    def validate_email(self, email):
        #users = mongo.db.user
        print(email.data)
        #user = users.find_one({'email': email.data})
        if user is None:
            raise ValidationError('There is no account with that email. You must register first')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    seller = BooleanField('Register as Seller')

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        #users = mongo.db.user
        user = users.find_one({'username': username.data})
        if user:
            raise ValidationError('That username is alreay taken. Please choose a different one')

    def validate_email(self, email):
        #users = mongo.db.user
        user = users.find_one({'email': email.data})
        if user:
            raise ValidationError('That email is already taken. Please choose a different one.')

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
    
#     def __repr__(self):
#         return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    status = db.Column(db.Boolean)
    role = db.Column(db.String(10), default='normal')
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username
