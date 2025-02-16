import sqlite3

# SQLite veritabanına bağlantı kurulması
con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()

# "kitaplik" adlı tablonun oluşturulması
# Eğer tablo mevcut değilse, yeniden oluşturulmadan var olan tablo kullanılacaktır.
def tablo_olustur():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kitaplik (
            İsim TEXT,
            Yazar TEXT,
            Yayınevi TEXT,
            Sayfa_Sayısı INT
        )
    """)
    con.commit()

tablo_olustur()

# Öntanımlı veri ekleme fonksiyonu
def veri_ekle():
    cursor.execute("""
        INSERT INTO kitaplik (İsim, Yazar, Yayınevi, Sayfa_Sayısı)
        VALUES ('İstanbul Hatırası', 'Ahmet Ümit', 'Everest', 561)
    """)
    con.commit()

# Parametre ile veri ekleme fonksiyonu
def veri_ekle2(isim, yazar, yayinevi, sayfa_sayisi):
    cursor.execute("""
        INSERT INTO kitaplik (İsim, Yazar, Yayınevi, Sayfa_Sayısı)
        VALUES (?, ?, ?, ?)
    """, (isim, yazar, yayinevi, sayfa_sayisi))
    con.commit()

# Kullanıcıdan kitap bilgilerini alma
isim = input("Kitap İsmi: ")
yazar = input("Yazar: ")
yayinevi = input("Yayınevi: ")
sayfa_sayisi = int(input("Sayfa Sayısı: "))

# Girilen verilerin veritabanına eklenmesi
veri_ekle2(isim, yazar, yayinevi, sayfa_sayisi)

# Veritabanı bağlantısının kapatılması
con.close()
