from  flask import Flask,render_template,redirect,url_for,flash
from blog.forms import RegisterForm
from blog import app,db
from blog.model import user

@app.route("/")
@app.route("/home")
def Home():
    return render_template("home.html",title="Home")


@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/user_register",methods=['GET','POST'])
def register1():
    form=RegisterForm()
    if form.validate_on_submit():
        newuser=user(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(newuser)
        db.session.commit()
        flash(f"account is created please login ","success")
        return redirect(url_for('about'))

    return render_template("register.html",form=form)
