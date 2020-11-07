# BIL372_Proje_16

## Kurulum
-python env oluştur
```
python -m venv env
env\Scripts\activate
```
-gerekli toolkitleri indir
```
pip install sqlAlchemy
pip install flask
pip install Flask-SQLAlchemy
pip install flask_login
pip install psycopg2

```
## Kurulum tamamlandıktan sonra çalıştırmak için
```
env\Scripts\activate (env aktif değilse önce onu aktif etmemiz gerekiyor)
set FLASK_APP=__init__.py
set FLASK_DEBUG=1
flask run
```
## ONEMLI
biletsepeti isminde bir db oluşturduktan sonra __init__.py dosyasında postgresPass için kendi root şifrenizi yazmış olmanız gerekiyor.
İlgili kısım;
```
    CONFIG = {
       'postgresUrl':'localhost:5432',
       'postgresUser':'postgres',
       'postgresPass':'123456', 
       'postgresDb':'biletsepeti',
    }
```
