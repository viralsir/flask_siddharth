from  flask import Flask,render_template,redirect,url_for,flash,request
from blog.forms import RegisterForm,LoginForm,UpdateForm
from blog import app,db
from blog.model import user
from flask_login import login_user,current_user,logout_user,login_required
import secrets
import os


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
        return redirect(url_for('login'))

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

def save_picture(form_picture):
    print("inside save_picture")
    random_hex=secrets.token_hex(8)
    f_name,f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+f_ext;
    picture_path=os.path.join(app.root_path,'static/profile_pics',picture_fn)
    form_picture.save(picture_path)
    return picture_fn;


@app.route("/account",methods=['GET','POST'])
@login_required
def account():
     form=UpdateForm()
     if form.validate_on_submit() :
         if form.picture.data :
             picture_name=save_picture(form.picture.data)
             current_user.image_fie=picture_name

         current_user.username=form.username.data
         current_user.email=form.email.data
         #db.session.add(current_user);
         db.session.commit();
         flash(f"Your accout has been updated.","success")
         print('redirect to home')
         return redirect(url_for("Home"))
     elif request.method=="GET" :
         form.username.data=current_user.username
         form.email.data=current_user.email

     image_file=url_for('static',filename='profile_pics/'+current_user.image_fie)
     return render_template("Account.html",image_file=image_file,form=form)