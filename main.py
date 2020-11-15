from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from sqlalchemy.sql import exists
from .models import BSUser
from . import db


main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html', name=current_user.username)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)


@main.route('/add_etkinlik')
def add_etkinlik_view():
	#products = Product.query.filter_by(is_active = True)
	return render_template('etkinlik.html',name=current_user.username, etkinlik=etkinlik)

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

@main.route('/etkinlik_list')
def etkinlik_list():
	#products = Product.query.filter_by(is_active = True) #aktif olan tüm productları alıyoruz ve product_list.html dosyasına products değişkeni ile gönderiyoruz
	return render_template('etkinlik_list.html',name=current_user.username, etkinlik=etkinlik)


