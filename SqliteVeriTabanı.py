import sqlite3

# SQLite veritabanına bağlan
con = sqlite3.connect("kütüphane.db")

# Veritabanı işlemleri için bir imleç (cursor) oluştur
cursor = con.cursor()

def tablo_olustur():
    """
    Eğer 'kitaplik' adlı bir tablo mevcut değilse, bu tabloyu oluşturur.
    Tabloda aşağıdaki sütunlar bulunur:
    - İsim (TEXT): Kitap adı
    - Yazar (TEXT): Kitabın yazarı
    - Yayınevi (TEXT): Kitabın yayınevi
    - Sayfa_Sayısı (INTEGER): Kitabın toplam sayfa sayısı
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kitaplik (
            İsim TEXT,
            Yazar TEXT,
            Yayınevi TEXT,
            Sayfa_Sayısı INTEGER
        )
    """)
    con.commit()

def veri_ekle():
    """Örnek bir kitabı 'kitaplik' tablosuna ekler."""
    cursor.execute("""
        INSERT INTO kitaplik VALUES ('İstanbul Hatırası', 'Ahmet Ümit', 'Everest', 561)
    """)
    con.commit()

def veri_ekle2(isim, yazar, yayinevi, sayfa_sayisi):
    """Parametre olarak verilen kitap bilgilerini 'kitaplik' tablosuna ekler."""
    cursor.execute("""
        INSERT INTO kitaplik VALUES (?, ?, ?, ?)
    """, (isim, yazar, yayinevi, sayfa_sayisi))
    con.commit()

def verileri_al():
    """'kitaplik' tablosundaki tüm kayıtları getirir ve ekrana yazdırır."""
    cursor.execute("SELECT * FROM kitaplik")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun içerikleri:")
    for kayit in liste:
        print(kayit)

def verileri_al2():
    """'kitaplik' tablosundaki kitap isimlerini ve yazarlarını getirir ve ekrana yazdırır."""
    cursor.execute("SELECT İsim, Yazar FROM kitaplik")
    liste = cursor.fetchall()
    for kayit in liste:
        print(kayit)

def verileri_al3(yayinevi):
    """Belirtilen yayınevine ait kitapları getirir ve ekrana yazdırır."""
    cursor.execute("SELECT * FROM kitaplik WHERE Yayınevi = ?", (yayinevi,))
    liste = cursor.fetchall()
    for kayit in liste:
        print(kayit)

# Örnek bir sorgu çalıştır
verileri_al3("Everest")

# Veritabanı bağlantısını kapat
con.close()
