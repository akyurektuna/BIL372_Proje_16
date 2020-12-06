DROP TABLE IF EXISTS indirim;

CREATE TABLE indirim(
	indirimkodu varchar(255) NOT NULL,
	etkinlikid varchar(255) NOT NULL,
	newprice int,
	PRIMARY KEY (indirimkodu),
	FOREIGN KEY (etkinlikid) REFERENCES ETKINLIK (etkinlikid) ON DELETE CASCADE ON UPDATE CASCADE
);