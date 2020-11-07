from flask_login import UserMixin
from . import db

class BSUser(UserMixin, db.Model): #databasedeki users tablosu elemanlarını tanıttık!
    userid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    userpassword = db.Column(db.String(100))
