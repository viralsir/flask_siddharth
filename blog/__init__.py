from  flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_marshmallow import Marshmallow


app=Flask(__name__)
db=SQLAlchemy(app)
ma=Marshmallow(app)

app.config['SECRET_KEY']='12345'
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:1234@localhost:5432/BLOGDB"
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from blog.forms import RegisterForm

from blog import routes
