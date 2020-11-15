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
## Miniworld Assumption
Bir etkinlik sisteminde konser ve tiyatro etkinlikleri tutulmaktadır. Bu sistemin üç çeşit user tipi vardır;
customer, admin, seller. User bunlardan birine ait olmak zorundadır ve sadece birine ait olabilir. Tüm
userlar için name, lastname, emailAddress ve userId tutulmaktadır. Customer userları etkinliklere
katılır ve ödeme yaparlar. Customer ve Etkinlik arasında N-M ilişki vardır. Seller tipi userlar için
userName ve password tutulmaktadır. Seller tipli userlar yeni konser ve/veya tiyatro etkinlikleri
yaratabilir ve yarattıkları etkinlikleri düzenleyebilirler. Seller ve Etkinlik arasında 1-N ilişki vardır.
Admin tipli userlar için userName ve password tutulmaktadır. Admin tipli userlar tüm etkinlikleri
yönetebilirler, etkinlikleri iptal edebilirler, sahneleri aktif ve/veya deaktif edebilirler. Admin ve Etkinlik
arasında 1-N ilişki vardır. Etkinliklerin düzenlendiği sahneler vardır. Sahneler stageName, address, city
ve isActive bilgileri ile tutulur. Sahne ve Etkinlik arasında 1-N ilişki vardır. Etkinlikler için biletler
konser ve tiyatro olarak ikiye ayrılmaktadır. Etkinlik bunlardan birine dahil olmak zorundadır ve en
fazla birine dahil olabilir. Tüm etkinlikler için stageName, name, city, time, price ve creator bilgileri
tutulmaktadır. Tiyatro biletleri için theatreId ve seatNumber tutulmaktadır. Tiyatro tipi etkinlikler için
Koltuklar theatreId, seatId ve isOccupied attributeları ile tutulur. Konser tipi etkinlikler için consertId,
regionNumber tutulmaktadır. Bölgeler Region tablosunda concertId, regionValue ve isOccupied
attributeları ile tutulur. Biletler için uygun olan ödeme yöntemleri tutulmaktadır. Yöntemler Payment
tablosunda ticketid ve paymentValue attributeları ile tutulur. Bilet ve payment arasında N-1 ilişki
vardır. Bazı etkinliklerde kullanıcılara indirim sağlanabilir. İndirimin miktarı ve indirimKodu
bulunmaktadır.

## EER 

![alt text](https://github.com/akyurektuna/BIL372_Proje_16/blob/main/eer.JPG)
