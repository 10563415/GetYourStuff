import os

import email_validator
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# from flask. import Moment
from flask_wtf import FlaskForm
from wtforms import (BooleanField, FileField, IntegerField, MultipleFileField,
                     PasswordField, StringField, SubmitField, TextAreaField,
                     validators)
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)
from flask import abort

SECRET_KEY = os.urandom(32)

import requests
from flask import (Blueprint, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)

from flask import session


app = Flask(__name__)
bootstrap = Bootstrap(app)
#moment = Moment(app)
app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = SECRET_KEY

# login_manager = LoginManager()
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'
# login_manager.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    user_agent = request.headers.get('User-Agent')
    if form.validate_on_submit():
        
        #######TODO: Insert function to check the token from fakeapi = if true redirect to search else login page with error
        ###if old_name is not None and old_name != form.name.data:
            ###flash('Looks like you have changed your name!')
        session['email'] = form.username.data
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
    email = session.get('email')
    url = "https://fakestoreapi.com/auth/login"
    req_body = {"username": "mor_2314","password": "83r5^"}
    resp = requests.post(url, data = req_body)
    #abort(404)
    return render_template('search.html', title='search')


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

