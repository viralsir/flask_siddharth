from flask_wtf.form import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length
from blog.model import user

class RegisterForm(FlaskForm):
    username=StringField("User Name :")
    email=StringField("Email :",validators=[DataRequired(),Email()])
    password=PasswordField("password :",validators=[DataRequired(),Length(min=8)])
    confirm_password=PasswordField("Confirm Password:",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("Register")

    def validate_username(self,username):
        newuser=user.query.filter_by(username=username.data).first();
        if newuser :
            raise ValueError('username is already taken please choose another one')

    def validate_email(self, email):
        newuser = user.query.filter_by(email=email.data).first();
        if newuser:
            raise ValueError('email is already taken please choose another one')
