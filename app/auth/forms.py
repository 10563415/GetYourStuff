from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

#Forms used for creating html components of login web page
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password',[
        validators.Regexp('^\w+$', message="Password must contain only letters, numbers or underscore"),
        validators.Length(min=5, max=25, message="Username must be betwen 5 & 25 characters"),
        validators.Required()

    ])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')



#Forms used for creating html components of registration web page
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])

    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.'),Regexp('^\w+$',0, message='Password must contain only letters, numbers or underscore'),Length(min=5, max=25, message="Username must be betwen 5 & 25 characters")])

    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


#Forms used for creating html components of change password web page
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.'),Regexp('^\w+$',0, message='Password must contain only letters, numbers or underscore'),Length(min=5, max=25, message="Username must be betwen 5 & 25 characters")])
    password2 = PasswordField('Confirm new password',
                              validators=[DataRequired()])
    submit = SubmitField('Update Password')



#Forms used for creating html components of reset password request web page
class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')



#Forms used for creating html components of password reset web page
class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.'),Regexp('^\w+$',0, message='Password must contain only letters, numbers or underscore'),Length(min=5, max=25, message="Username must be betwen 5 & 25 characters")])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')


#Forms used for creating html components of change email web page
class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')
