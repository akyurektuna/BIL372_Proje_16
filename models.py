from flask_login import UserMixin
from . import db

class BSUser(UserMixin, db.Model): #databasedeki users tablosu elemanlarını tanıttık!
    userid = db.Column(db.String(100), primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    userpassword = db.Column(db.String(100))
    def get_id(self):
        return self.userid

class Customer(db.Model):
    customerid = db.Column(db.String(100),primary_key=True)
    def get_id(self):
        return self.customerid

class Seller(db.Model):
    sellerid = db.Column(db.String(100),primary_key=True)
    companyname = db.Column(db.String(100))
    def get_id(self):
        return self.sellerid