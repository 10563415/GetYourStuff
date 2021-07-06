from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ..models import User


# class LoginForm(FlaskForm):
#     username = StringField('User', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Request Reset Password')

#     def validate_email(self, email):
#         #users = mongo.db.user
#         print(email.data)
#         #user = users.find_one({'email': email.data})
#         if user is None:
#             raise ValidationError('There is no account with that email. You must register first')


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
