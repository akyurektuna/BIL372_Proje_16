from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    CONFIG = {
       'postgresUrl':'localhost:5432',
       'postgresUser':'postgres',
       'postgresPass':'123456', #tuna icin 123456
       'postgresDb':'biletsepeti',
    }

    POSTGRES_URL = CONFIG['postgresUrl']
    POSTGRES_USER = CONFIG['postgresUser']
    POSTGRES_PASS = CONFIG['postgresPass']
    POSTGRES_DB = CONFIG['postgresDb']
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PASS, url=POSTGRES_URL, db=POSTGRES_DB)
    app.config['SECRET_KEY'] = '1'

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import BSUser

    @login_manager.user_loader
    def load_user(userid):
        return BSUser.query.get(userid)

    #session!
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
