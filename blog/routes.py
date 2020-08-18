from  flask import Flask,render_template,redirect,url_for,flash,request
from blog.forms import RegisterForm,LoginForm
from blog import app,db
from blog.model import user
from flask_login import login_user,current_user,logout_user,login_required

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
    if current_user.is_authenticated :
        return redirect(url_for('Home'))
    if form.validate_on_submit():
        newuser=user(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(newuser)
        db.session.commit()
        flash(f"account is created please login ","success")
        return redirect(url_for('about'))

    return render_template("register.html",form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    if form.validate_on_submit():
        nuser=user.query.filter_by(email=form.email.data , password=form.password.data).first();
        if nuser :
            login_user(nuser,remember=form.remember_me.data)
            next=request.args.get("next")
            print(next)
            if next :
                 flash(f"login successfully ", "success")
                 return redirect(next)
            else :
                 flash(f"login successfully ","success")
                 return redirect(url_for('Home'))
        else :
            flash("username or password are incorrect","danger")
    return render_template("login.html",title="Login",form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route("/account")
@login_required
def account():
     return render_template("Account.html")