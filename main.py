from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from sqlalchemy.sql import exists
from .models import *
from . import db


main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    seller = Seller.query.filter_by(sellerid=current_user.userid).first()
    customer = Customer.query.filter_by(customerid=current_user.userid).first()
    if seller:
        return render_template('indexSeller.html', name=current_user.username)
    elif customer:
        return render_template('indexCustomer.html', name=current_user.username)
    return render_template('index.html', name=current_user.username)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)


@main.route('/add_etkinlik')
def add_etkinlik_view():
	return render_template('etkinlik.html',name=current_user.username)

@main.route('/add_etkinlik', methods=['POST'])
def add_etkinlik():
	"""
    m_syscode = request.form.get('m_syscode')
	m_code = request.form.get('m_code')
	m_name = request.form.get('m_name')
	m_shortname = request.form.get('m_shortname')
	m_parentcode = request.form.get('parent') 
	m_abstract = True if request.form.get('m_abstract') else False
	m_category = request.form.get('m_category')
	is_active = 1

	product = Product.query.filter_by(m_syscode=m_syscode).first()

	if product:
		flash('Product already exist')
		return redirect(url_for('main.product_list'))

	new_product = Product(m_syscode=m_syscode, m_code=m_code, m_name=m_name, m_shortname=m_shortname, m_parentcode=m_parentcode, m_abstract=m_abstract, m_category=m_category, is_active=is_active)

	db.session.add(new_product)
	db.session.commit()
    """
	return redirect(url_for('main.etkinlik_list'))

@main.route('/add_sahne')
def add_sahne_view():
	return render_template('addSahne.html',name=current_user.username)

@main.route('/add_sahne', methods=['POST'])
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
    
    return redirect(url_for('main.index'))


@main.route('/etkinlik_list')
def etkinlik_list():
	#products = Product.query.filter_by(is_active = True) #aktif olan tüm productları alıyoruz ve product_list.html dosyasına products değişkeni ile gönderiyoruz
	return render_template('etkinlik_list.html',name=current_user.username, etkinlik=etkinlik)


