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
    #if form.validate_on_submit():
        #check_user = User.objects(email=form.email.data).first()
        #if check_user and check_password_hash(check_user['password'], form.password.data):
            #login_user(check_user)
            #id = current_user.get_id()
            #user_document=mongo.db.user.find_one({'_id':ObjectId(id)},{'_id':0,'role':1})
            #if user_document['role']=='admin':
             #   return redirect('/admin_')
            #flash('You have been successfully logged in', 'success')
            #next_page = request.args.get('next')
            #return redirect(next_page) if next_page else redirect(url_for('main.home'))
        #else:
            #flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='login', form=form)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
