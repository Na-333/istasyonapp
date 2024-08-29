import sqlite3
baglanti = sqlite3.connect("OPET.db")
cs = baglanti.cursor()

cs.execute("insert into admin(id,kullanici,sifre) values(?,?,?)",(1,"fahrisozer","as1234"))
baglanti.commit()