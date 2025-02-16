import sqlite3

# SQLite veritabanına bağlantı kurulması
con = sqlite3.connect("kütüphane.db")

# Veritabanı işlemleri için bir cursor (imleç) oluşturulması
cursor = con.cursor()

# Tablo oluşturma fonksiyonu
def tablo_olustur():
    """
    Eğer 'kitaplik' adında bir tablo mevcut değilse, bu tabloyu oluşturur.
    Tablo, aşağıdaki sütunlardan oluşmaktadır:
        - İsim (Metin)
        - Yazar (Metin)
        - Yayınevi (Metin)
        - Sayfa Sayısı (Tamsayı)
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kitaplik (
            İsim TEXT,
            Yazar TEXT,
            Yayınevi TEXT,
            Sayfa_Sayısı INT
        )
    """)
    # Yapılan değişikliklerin veritabanına işlenmesi
    con.commit()

# Fonksiyon çağrılarak tablonun oluşturulması
tablo_olustur()

# Veritabanı bağlantısının kapatılması
con.close()
