from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from sqlalchemy.sql import exists
from .models import *
from . import db
from sqlalchemy import exc


main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    seller = Seller.query.filter_by(sellerid=current_user.userid).first()
    customer = Customer.query.filter_by(customerid=current_user.userid).first()
    admin = BSAdmin.query.filter_by(adminid=current_user.userid).first()
    if seller:
        return render_template('indexSeller.html', name=current_user.username)
    elif customer:
        return render_template('indexCustomer.html', name=current_user.username)
    elif admin:
        return render_template('indexAdmin.html', name=current_user.username)
    return render_template('index.html', name=current_user.username)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)


@main.route('/add_etkinlik')
def add_etkinlik_view():

    sahneler = Sahne.query.all()
    return render_template('etkinlik.html',name=current_user.username,sahneler=sahneler)

@main.route('/add_etkinlik', methods=['POST']) #bu method seller icin yazilmistir
def add_etkinlik():
	
    stagename = request.form.get('stagename')
    etkinlikname = request.form.get('etkinlikName')
    price = request.form.get('price')
    etkinlikdate = request.form.get('etkinlikDate')
    city = request.form.get('city') 
    etkinlikType = request.form.get('etkinlikType')
    creator = current_user.userid
	
	
    max_id = db.session.query(db.func.max(Etkinlik.etkinlikid)).scalar() #max_id yi buluyor
    
    if max_id is None:
        max_id = str(0)
    else:
        max_id = str(int(max_id) + 1) #burada numeric string inc edildi


    if etkinlikType=='tiyatro':
        new_etkinlik = Etkinlik(etkinlikid= max_id,creator=creator, systemadmin='0', stagename=stagename, etkinlikname=etkinlikname, price=price, etkinlikdate=etkinlikdate, city=city)
        db.session.add(new_etkinlik)
        db.session.commit()
        new_etkinlik_tiyatro = Tiyatro(theatreid=max_id)
        db.session.add(new_etkinlik_tiyatro)
    elif etkinlikType=='konser':
        new_etkinlik = Etkinlik(etkinlikid= max_id,creator=creator, systemadmin='0', stagename=stagename, etkinlikname=etkinlikname, price=price, etkinlikdate=etkinlikdate, city=city)
        db.session.add(new_etkinlik)
        db.session.commit()
        new_etkinlik_konser = Konser(concertid=max_id)
        db.session.add(new_etkinlik_konser)
    
    db.session.commit()
    if creator=='0':
        return redirect(url_for('main.etkinlik_list_admin'))
    return redirect(url_for('main.etkinlik_list'))

@main.route('/add_etkinlik_admin')
def add_etkinlik_admin_view():
    sahneler = Sahne.query.all()
    return render_template('etkinlikAdmin.html',name=current_user.username,sahneler=sahneler)

@main.route('/add_etkinlik_admin', methods=['POST']) #bu method admin icin yazilmistir
def add_etkinlik_admin():
	
    stagename = request.form.get('stagename')
    etkinlikname = request.form.get('etkinlikName')
    price = request.form.get('price')
    etkinlikdate = request.form.get('etkinlikDate')
    city = request.form.get('city') 
    etkinlikType = request.form.get('etkinlikType')
    creator = current_user.userid
	
	
    max_id = db.session.query(db.func.max(Etkinlik.etkinlikid)).scalar() #max_id yi buluyor
    
    if max_id is None:
        max_id = str(0)
    else:
        max_id = str(int(max_id) + 1) #burada numeric string inc edildi


    if etkinlikType=='tiyatro':
        new_etkinlik = Etkinlik(etkinlikid= max_id,creator=creator, systemadmin='0', stagename=stagename, etkinlikname=etkinlikname, price=price, etkinlikdate=etkinlikdate, city=city)
        db.session.add(new_etkinlik)
        db.session.commit()
        new_etkinlik_tiyatro = Tiyatro(theatreid=max_id)
        db.session.add(new_etkinlik_tiyatro)
    elif etkinlikType=='konser':
        new_etkinlik = Etkinlik(etkinlikid= max_id,creator=creator, systemadmin='0', stagename=stagename, etkinlikname=etkinlikname, price=price, etkinlikdate=etkinlikdate, city=city)
        db.session.add(new_etkinlik)
        db.session.commit()
        new_etkinlik_konser = Konser(concertid=max_id)
        db.session.add(new_etkinlik_konser)
    
    db.session.commit()
    if creator=='0':
        return redirect(url_for('main.etkinlik_list_admin'))
    return redirect(url_for('main.etkinlik_list'))


@main.route('/add_sahne')
def add_sahne_view():
	return render_template('addSahne.html',name=current_user.username)

@main.route('/add_sahne', methods=['POST']) #bu method seller icin yazildi
def add_sahne():
	
    stageName = request.form.get('stageName')
    adres = request.form.get('adres')
    city = request.form.get('city')
    isActive = request.form.get('isActive')
	
    sahne = Sahne.query.filter_by(stagename=stageName).first()

    if sahne:
        flash('Stage already exist')
        return redirect(url_for('main.add_sahne'))
    if isActive=='yes':
        new_stage = Sahne(stagename=stageName, adres=adres, city=city, isactive=True)       
    elif isActive=='no':
        new_stage = Sahne(stagename=stageName, adres=adres, city=city, isactive=False)

    db.session.add(new_stage)
    db.session.commit()
    return redirect(url_for('main.sahne_list'))

@main.route('/add_sahne_admin')
def add_sahne_admin_view():
	return render_template('addSahneAdmin.html',name=current_user.username)

@main.route('/add_sahne_admin', methods=['POST']) #bu method admin icin yazildi
def add_sahne_admin():
	
    stageName = request.form.get('stageName')
    adres = request.form.get('adres')
    city = request.form.get('city')
    isActive = request.form.get('isActive')
	
    sahne = Sahne.query.filter_by(stagename=stageName).first()

    if sahne:
        flash('Stage already exist')
        return redirect(url_for('main.add_sahne_admin'))
    if isActive=='yes':
        new_stage = Sahne(stagename=stageName, adres=adres, city=city, isactive=True)       
    elif isActive=='no':
        new_stage = Sahne(stagename=stageName, adres=adres, city=city, isactive=False)

    db.session.add(new_stage)
    db.session.commit()
    return redirect(url_for('main.sahne_list_admin'))

@main.route('/sahne_list')
def sahne_list():
	sahne = Sahne.query.filter_by(isactive = True) #aktif olan tüm sahneleri alıyoruz ve sahneList.html dosyasına sahne değişkeni ile gönderiyoruz
	return render_template('sahneList.html',name=current_user.username, sahne=sahne)

@main.route('/sahne_list_admin')
def sahne_list_admin():
	sahne = Sahne.query.all() #admin tum sahneleri gorebilir, aktif veya deaktif bilgilerini de gorebilir.
	return render_template('sahneListAdmin.html',name=current_user.username, sahne=sahne)

@main.route('/etkinlik_list')
def etkinlik_list():
	etkinlik = Etkinlik.query.filter_by(creator = current_user.userid) #Seller kendi yarattığı etkinlikleri görebiliyor.
	return render_template('etkinlik_list.html',name=current_user.username, etkinlik=etkinlik)

@main.route('/etkinlik_list_customer')
def etkinlik_list_customer():
	etkinlik = Etkinlik.query.all() #Customer tüm etkinlikleri görebiliyor ancak farklı bir base navbar kullanıyor dolayısıyla yeni bir etkinlik list sayfası eklendi.
	return render_template('etkinlik_list_customer.html',name=current_user.username, etkinlik=etkinlik)

@main.route('/etkinlik_list_admin')
def etkinlik_list_admin():
	etkinlik = Etkinlik.query.all() #Admin yaratılan tüm etkinlikleri görebiliyor.
	return render_template('etkinlik_list_admin.html',name=current_user.username, etkinlik=etkinlik)

@main.route('/buy_ticket/<id>')
def buy_ticket_view(id):
    etkinlik = Etkinlik.query.get(id)
    konserMi = db.session.query(db.exists().where(Konser.concertid == id)).scalar()
    tiyatroMu = db.session.query(db.exists().where(Tiyatro.theatreid == id)).scalar()
    return render_template('buy_ticket.html',name=current_user.username,etkinlik=etkinlik,konserMi=konserMi,tiyatroMu=tiyatroMu)

@main.route('/buy_ticket/<id>/', methods = ['POST'])
def buy_ticket(id):
    etkinlikname = request.form.get('etkinlikname')
    konserMi = db.session.query(db.exists().where(Konser.concertid == id)).scalar()
    tiyatroMu = db.session.query(db.exists().where(Tiyatro.theatreid == id)).scalar()

    max_id = db.session.query(db.func.max(Bilet.ticketid)).scalar() #max_id yi buluyor
    
    if max_id is None:
        max_id = str(0)
    else:
        max_id = str(int(max_id) + 1) #burada numeric string inc edildi

    new_bilet = Bilet(ticketid= max_id, etkinlikid=id)
    db.session.add(new_bilet)
    #db.session.commit()

    if konserMi:
        regionvalue = request.form.get('regionvalue')
        new_konserbilet = Konserbileti(kbiletid=max_id,concertid=id,regionvalue=regionvalue,userid=current_user.userid)
        db.session.add(new_konserbilet)
    
    elif tiyatroMu:
        seatnumber = request.form.get('seatnumber')
        new_tiyatrobilet = Tiyatrobileti(tbiletid=max_id,theatreid=id,seatnumber=seatnumber,userid=current_user.userid)
        db.session.add(new_tiyatrobilet)
	
    db.session.commit()
    return redirect(url_for('main.etkinlik_list_customer'))
    #user icin biletler sayfası ekleyince redirect(url_for('main.user_bilet_list'))

@main.route('/list_user_tickets')
def list_user_tickets():
    #ticketskonser = Konserbileti.query.filter_by(userid = current_user.userid) 
    #ticketstiyatro = Tiyatrobileti.query.filter_by(userid = current_user.userid)
    join_etkinlikKonser = db.session.query(Etkinlik, Konserbileti).join(Etkinlik, (Etkinlik.etkinlikid == Konserbileti.concertid) & (Konserbileti.userid == current_user.userid))\
        .add_columns(Etkinlik.etkinlikname,Etkinlik.stagename,Etkinlik.city,Etkinlik.price,Etkinlik.etkinlikdate,Konserbileti.regionvalue).all()
    join_etkinlikTiyatro = db.session.query(Etkinlik, Tiyatrobileti).join(Tiyatrobileti, (Etkinlik.etkinlikid == Tiyatrobileti.theatreid) &(Tiyatrobileti.userid == current_user.userid))\
        .add_columns(Etkinlik.etkinlikname,Etkinlik.stagename,Etkinlik.city,Etkinlik.price,Etkinlik.etkinlikdate,Tiyatrobileti.seatnumber).all()
    return render_template('list_user_tickets.html',join_etkinlikKonser=join_etkinlikKonser,join_etkinlikTiyatro=join_etkinlikTiyatro)
