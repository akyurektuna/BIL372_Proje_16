# BIL372_Proje_16

kurulum;
-python env oluştur
python -m venv env
env\Scripts\activate

-gerekli toolkitleri indir
pip install sqlAlchemy
pip install flask
pip install Flask-SQLAlchemy
pip install flask_login
pip install psycopg2

---buraya kadar kurulum tamamlandıktan sonra çalıştırmak için;
set FLASK_APP=__init__.py
set FLASK_DEBUG=1
flask run
