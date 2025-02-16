import sqlite3

class KutuphaneVeritabani:
    def __init__(self, veritabani_adi="kutuphane.db"):
        """
        SQLite veritabanına bağlanır ve bir imleç (cursor) oluşturur.
        """
        self.con = sqlite3.connect(veritabani_adi)
        self.cursor = self.con.cursor()
        self.tablo_olustur()
    
    def tablo_olustur(self):
        """
        Eğer kitaplık tablosu yoksa, oluşturur.
        """
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS kitaplik (
                Isim TEXT,
                Yazar TEXT,
                Yayinevi TEXT,
                Sayfa_Sayisi INTEGER
            )
            """
        )
        self.con.commit()
    
    def veri_ekle(self, isim, yazar, yayinevi, sayfa_sayisi):
        """
        Kitaplık tablosuna yeni bir kayıt ekler.
        """
        self.cursor.execute(
            "INSERT INTO kitaplik VALUES (?, ?, ?, ?)", (isim, yazar, yayinevi, sayfa_sayisi)
        )
        self.con.commit()
    
    def verileri_al(self):
        """
        Kitaplık tablosundaki tüm kayıtları getirir.
        """
        self.cursor.execute("SELECT * FROM kitaplik")
        return self.cursor.fetchall()
    
    def verileri_filtrele(self, yayinevi):
        """
        Belirtilen yayınevine ait kitapları getirir.
        """
        self.cursor.execute("SELECT * FROM kitaplik WHERE Yayinevi = ?", (yayinevi,))
        return self.cursor.fetchall()
    
    def verileri_guncelle(self, eski_yayinevi, yeni_yayinevi):
        """
        Belirtilen yayınevinin ismini günceller.
        """
        self.cursor.execute(
            "UPDATE kitaplik SET Yayinevi = ? WHERE Yayinevi = ?", (yeni_yayinevi, eski_yayinevi)
        )
        self.con.commit()
    
    def verileri_sil(self, yazar):
        """
        Belirtilen yazara ait kitapları veri tabanından siler.
        """
        self.cursor.execute("DELETE FROM kitaplik WHERE Yazar = ?", (yazar,))
        self.con.commit()
    
    def baglantiyi_kapat(self):
        """
        Veritabanı bağlantısını kapatır.
        """
        self.con.close()

# Örnek Kullanım
if __name__ == "__main__":
    db = KutuphaneVeritabani()
    db.veri_ekle("İstanbul Hatırası", "Ahmet Ümit", "Everest", 561)
    db.veri_ekle("Kürk Mantolu Madonna", "Sabahattin Ali", "YKY", 160)
    
    print("Tüm Kayıtlar:")
    for kitap in db.verileri_al():
        print(kitap)
    
    print("\nEverest Yayınevi Kitapları:")
    for kitap in db.verileri_filtrele("Everest"):
        print(kitap)
    
    db.verileri_guncelle("YKY", "Yapı Kredi Yayınları")
    db.verileri_sil("Ahmet Ümit")
    db.baglantiyi_kapat()
