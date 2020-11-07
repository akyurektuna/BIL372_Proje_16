from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import BSUser
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')



@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email') #formdaki email alanından gelenler buraya
    password = request.form.get('userpassword')
    remember = True if request.form.get('remember') else False

    user = BSUser.query.filter_by(email=email).first()

    #user emaili var mı diye kontrol
    if not user or not check_password_hash(user.userpassword, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # user yoksa tekrar login sayfası

    # üst ifi atlattıysak index'e geçebiliriz!
    login_user(user, remember=remember)
    return redirect(url_for('main.index')) #main.index main.py dosyasındaki index metodu!!!

@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    userpassword = request.form.get('userpassword')

    user = BSUser.query.filter_by(email=email).first() # email kayıtlı mı diye bakıyoruz

    max_id = db.session.query(db.func.max(BSUser.userid)).scalar() #max_id yi buluyor

    if max_id is None:
        max_id = 0
    else:
        max_id = max_id+1

    if user: # eger mail önceden kayıtlı ise hata
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))


    # user kayıtlı degilse kayıt ediyoruz!
    new_user = BSUser(userid= max_id,email=email, firstname=firstname, lastname=lastname, username=username, userpassword=generate_password_hash(userpassword, method='sha256'))


    # database'e ekleme işlemi commit edilmeli
    db.session.add(new_user)
    db.session.commit()


    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
