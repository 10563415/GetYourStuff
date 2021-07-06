from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user

from ..models import User
from . import auth
from .forms import LoginForm


@auth.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and not user.verify_password(form.password.data):  ##TODO: remove NOT from verify password
            login_user(user, form.remember.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.search')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


from flask_login import login_required, logout_user
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

