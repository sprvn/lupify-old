from lupify import db

from flask_login import UserMixin

class User(UserMixin):
    #id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return '<User %r' % (self.username)