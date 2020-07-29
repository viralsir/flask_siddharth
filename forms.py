from flask_wtf.form import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length


class RegisterForm(FlaskForm):
    username=StringField("User Name :")
    email=StringField("Email :",validators=[DataRequired(),Email()])
    password=PasswordField("password :",validators=[DataRequired(),Length(min=8)])
    confirm_password=PasswordField("Confirm Password:",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("Register")

