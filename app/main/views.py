from flask import render_template, session, redirect, url_for, current_app,request
# from .. import db
from ..models import User
#from ..email import send_email
from . import main
from .forms import LoginForm,RegistrationForm,RequestResetForm
import requests

@main.route('/', methods=['GET', 'POST'])
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

@main.route('/search', methods=['GET', 'POST'])
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


@main.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
        form = RequestResetForm()
        response_API = requests.get('https://www.askpython.com/')
        response_API.status_code
        return render_template('reset_request.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
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

@main.route('/user/<name>/<comments>')
def user(name,comments):
    return render_template('user.html', name=name,comments=comments)