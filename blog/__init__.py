from  flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SECRET_KEY']='12345'
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:1234@localhost:5432/BLOGDB"

from blog.forms import RegisterForm

from blog import routes
