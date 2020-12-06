from flask_login import UserMixin
from datetime import datetime
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

class BSAdmin(db.Model):
    adminid = db.Column(db.String(100),primary_key=True)
    def get_id(self):
        return self.adminid

class Bilet(db.Model):
    ticketid = db.Column(db.String(100),primary_key=True)
    etkinlikid = db.Column(db.String(100))
    def get_id(self):
        return self.ticketid

class CustomerEtkinlik(db.Model):
    userid = db.Column(db.String(100),primary_key=True)
    etkinlikid = db.Column(db.String(100),primary_key=True)

class Etkinlik(db.Model):
    etkinlikid = db.Column(db.String(100),primary_key=True)
    creator = db.Column(db.String(100))
    systemadmin = db.Column(db.String(100))
    stagename = db.Column(db.String(100))
    etkinlikname = db.Column(db.String(100))
    price = db.Column(db.Integer())
    etkinlikdate = db.Column(db.DateTime())
    city = db.Column(db.String(100))
    def get_id(self):
        return self.etkinlikid

class Indirim(db.Model):
    indirimkodu = db.Column(db.String(100),primary_key=True)
    etkinlikid = db.Column(db.String(100))
    newprice = db.Column(db.Integer())
    def get_id(self):
        return self.indirimkodu

class Koltuk(db.Model):
    seatid = db.Column(db.String(100),primary_key=True)
    theatreid = db.Column(db.String(100))
    isoccupied = db.Column(db.Boolean())
    def get_id(self):
        return self.seatid

class Konser(db.Model):
    concertid = db.Column(db.String(100),primary_key=True)
    def get_id(self):
        return self.concertid

class Konserbileti(db.Model):
    kbiletid = db.Column(db.String(100),primary_key=True) #bilet tablosuyla bagladigimiz pkey
    concertid = db.Column(db.String(100)) #konser tablosuyla bagladigimiz fkey
    userid = db.Column(db.String(100)) #user tablosuyla bagladigimiz fkey
    regionvalue = db.Column(db.Integer())
    def get_id(self):
        return self.concertid

class Payment(db.Model):
    paymentid = db.Column(db.String(100),primary_key=True)
    ticketid = db.Column(db.String(100))
    paymentvalue = db.Column(db.Integer())
    def get_id(self):
        return self.paymentid

class Region(db.Model):
    regionid = db.Column(db.String(100),primary_key=True)
    concertid = db.Column(db.String(100))
    regionsection = db.Column(db.Integer())
    isoccupied = db.Column(db.Boolean())
    def get_id(self):
        return self.regionid

class Sahne(db.Model):
    stagename = db.Column(db.String(100),primary_key=True)
    adres = db.Column(db.String(100))
    city = db.Column(db.String(100))
    isactive = db.Column(db.Boolean())
    def get_id(self):
        return self.stagename

class Tiyatro(db.Model):
    theatreid = db.Column(db.String(100),primary_key=True)
    def get_id(self):
        return self.theatreid

class Tiyatrobileti(db.Model):
    tbiletid = db.Column(db.String(100),primary_key=True)
    theatreid = db.Column(db.String(100))
    userid = db.Column(db.String(100), primary_key=True)
    seatnumber = db.Column(db.Integer())
    def get_id(self):
        return self.theatreid