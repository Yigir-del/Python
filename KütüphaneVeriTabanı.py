import sqlite3

class Kitap:
    def __init__(self, adi, yazari, baski, yayinevi, sayfa_sayisi):
        self.adi = adi
        self.yazari = yazari
        self.baski = baski
        self.yayinevi = yayinevi
        self.sayfa_sayisi = sayfa_sayisi

    def __str__(self):
        return "{}  {}  {}  {}  {}".format(self.adi, self.yazari, self.baski, self.yayinevi, self.sayfa_sayisi)

class KutuphaneVeriTabani:
    def __init__(self):
        self.baglanti_kur()

    def baglanti_kur(self):
        self.baglanti = sqlite3.connect("kutuphane.db")
        self.cursor = self.baglanti.cursor()

        sorgu = """CREATE TABLE IF NOT EXISTS kitaplik (
            kitap_adi TEXT,
            yazar_adi TEXT,
            baski INT,
            yayinevi TEXT,
            sayfa_sayisi INT
        )"""
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()
        print("Bağlantı kesildi.")

    def kitaplari_goster(self):
        sorgu = "SELECT * FROM kitaplik"
        self.cursor.execute(sorgu)
        liste = self.cursor.fetchall()

        if not liste:
            print("Kitaplığınız boş.")
        else:
            print("Tüm kitaplarınız:")
            for kitap in liste:
                print(kitap)

    def kitap_sorgula(self, isim):
        sorgu = "SELECT * FROM kitaplik WHERE kitap_adi = ?"
        self.cursor.execute(sorgu, (isim,))
        liste = self.cursor.fetchall()

        if not liste:
            print("Aradığınız kitap sistemde bulunmamaktadır.")
        else:
            print("Aradığınız kitap:")
            for kitap in liste:
                print(kitap)

    def kitap_ekle(self, adi, yazari, baski, yayinevi, sayfa_sayisi):
        self.kitap = Kitap(adi, yazari, baski, yayinevi, sayfa_sayisi)
        sorgu = "INSERT INTO kitaplik VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(sorgu, (self.kitap.adi, self.kitap.yazari, self.kitap.baski, self.kitap.yayinevi, self.kitap.sayfa_sayisi))
        self.baglanti.commit()

    def kitap_sil(self, kitap_adi):
        sorgu = "DELETE FROM kitaplik WHERE kitap_adi = ?"
        self.cursor.execute(sorgu, (kitap_adi,))
        self.baglanti.commit()

    def baski_yukselt(self, kitap_adi, yeni_baski):
        sorgu = "UPDATE kitaplik SET baski = ? WHERE kitap_adi = ?"
        self.cursor.execute(sorgu, (yeni_baski, kitap_adi))
        self.baglanti.commit()


# Örnek kullanım
k = KutuphaneVeriTabani()
k.kitap_ekle("İstanbul Hatırası", "Ahmet Ümit", 1, "Everest", 561)
k.kitaplari_goster()
k.kitap_sorgula("İstanbul Hatırası")
k.baski_yukselt("İstanbul Hatırası", 2)
k.kitaplari_goster()
k.kitap_sil("İstanbul Hatırası")
k.kitaplari_goster()
k.baglantiyi_kes()
