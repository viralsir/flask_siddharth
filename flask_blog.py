from  flask import Flask,render_template,redirect,url_for
from forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SECRET_KEY']='12345'
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:1234@localhost:5432/BLOGDB"

posts=[
    {
        "author":"vimal shah",
        "title":"First post",
        "content":"first post content ",
        "date_posted":" 12 feb 2020"
    }
    ,
    {
        "author":"viren shah",
        "title":"second post",
        "content":"second post content ",
        "date_posted":" 12 feb 2020"
    }
]

@app.route("/")
@app.route("/home")
def Home():
    return render_template("home.html",posts=posts,title="Home")


@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/user_register",methods=['GET','POST'])
def register1():
    form=RegisterForm()
    if form.validate_on_submit():
        title="about - "+ str(form.username)
        return redirect(url_for('about'),title=title)

    return render_template("register.html",form=form)



if __name__ == '__main__':
    app.run(debug=True)