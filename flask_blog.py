from  flask import Flask,render_template

app=Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)