from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# from flask. import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, FileField, MultipleFileField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator

import os
SECRET_KEY = os.urandom(32)



app = Flask(__name__)
bootstrap = Bootstrap(app)
#moment = Moment(app)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


@app.route('/user/<name>/<comments>')
def user(name,comments):
    return render_template('user.html', name=name,comments=comments)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
        form = RequestResetForm()
        return render_template('reset_request.html', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
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

