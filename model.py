from flask_blog import db

class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(30),nullable=False,unique=True)
    password=db.Column(db.String(15),nullable=False)

    def __str__(self):
        return f"User({self.username},{self.email})"
