import sqlite3

class Sarki:
    def __init__(self, Sarki_ismi, Sanatci, Album, Produksiyon_Sirketi, Sarki_Suresi):
        self.sarki_ismi = Sarki_ismi
        self.sanatci = Sanatci
        self.album = Album
        self.produksiyon_sirketi = Produksiyon_Sirketi
        self.sarki_suresi = Sarki_Suresi

    def __str__(self):
        return "{}  {}  {}  {}  {}".format(self.sarki_ismi, self.sanatci, self.album, self.produksiyon_sirketi, self.sarki_suresi)

class Sanatci:
    def __init__(self):
        self._baglanti_kur()

    def _baglanti_kur(self):
        self.con = sqlite3.connect("Sarkici.db")
        self.cursor = self.con.cursor()

    def _tablo_olustur(self, tablo_adi):
        self.tablo_adi = tablo_adi
        sorgu1 = f"""CREATE TABLE IF NOT EXISTS {str(self.tablo_adi)}
        (   
            sarki_ismi TEXT,
            sanatci TEXT,
            album TEXT,
            prod TEXT,
            sure INT
        )"""
        self.cursor.execute(sorgu1)
        print("Tablo olusturuldu. ")
        sorgu2 = f"PRAGMA table_info({self.tablo_adi})"
        self.cursor.execute(sorgu2)
        sutunlar = self.cursor.fetchall()
        sutun_bilgileri = [(sutun[0], sutun[1], sutun[2]) for sutun in sutunlar]
        for i in sutun_bilgileri:
            print(i)
        self.con.commit()

    def _baglantiyi_kes(self):
        print("Baglanti kesiliyor..")
        self.con.close()

    def sarki_ekle(self, Sarki_ismi, Album, Produksiyon_Sirketi, Sarki_Suresi):
        sarki = Sarki(Sarki_ismi, self.tablo_adi, Album, Produksiyon_Sirketi, Sarki_Suresi)
        sorgu = f"INSERT into {self.tablo_adi} Values(?,?,?,?,?)"
        self.cursor.execute(sorgu, (sarki.sarki_ismi, sarki.sanatci, sarki.album, sarki.produksiyon_sirketi, sarki.sarki_suresi))
        self.con.commit()
        print("Sarki eklendi..")

    def sarki_sil(self,sarki_ismi):
        sorgu = f"Delete from {self.tablo_adi} where sarki_ismi = ?"
        self.cursor.execute(sorgu,(sarki_ismi,))
        self.con.commit()

    def sarkileri_bastir(self):
        sorgu = f"SELECT * from {self.tablo_adi}"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
        if sarkilar == []:
            print("Sarki listesi bos.")
            return 0
        else:
            print("Sarkilar bastiriliyor.")
            for i in sarkilar:
                print(i)
            return 1

    def toplam_sure(self):
        sorgu = f"Select sure from {self.tablo_adi}"
        self.cursor.execute(sorgu)
        liste = self.cursor.fetchall()
        counter = 0
        for i in liste:
            counter += int(i[0])
        print(f"Toplam sarki suresi: {counter}")


# Ana program akışı
sanatci = Sanatci()

print("""
Sanatci Veritabanina hosgeldiniz..

Cikmak icin --> 'q'
Sanatci kitapligi olusturmak veya varolan kitapligi acmak  icin --> 1    
Sarki eklemek icin --> 2
Sarkileri gormek icin --> 3
Sarki silmek icin --> 4
Toplam sarki suresi --> 5
""")

itablo_adi = ""
while True:
    print("Ana menudesiniz")
    op = input()
    
    if op == 'q':
        sanatci._baglantiyi_kes()
        break
    
    if op == "1":
        itablo_adi = input("Sanatci adini giriniz: ")
        sanatci._tablo_olustur(tablo_adi=itablo_adi)
    
    if op == "2":
        if itablo_adi == "":
            print("Sanatci bilgisi girilmedi.")
            continue  # Sanatçı bilgisi girilmediyse döngüye devam et
    
        else:
            Sarki_ismi = input("Sarki adi: ")
            Album = input("Album adi: ")
            Produksiyon_Sirketi = input("Prod sirketi: ")
            try:
                Sarki_Suresi = input("Sarki suresi: ")
            except ValueError:
                print("Gecersiz sure. Lutfen int deger giriniz.")
                continue
            sanatci.sarki_ekle(Sarki_ismi, Album, Produksiyon_Sirketi, Sarki_Suresi)
            sanatci.sarkileri_bastir()
    
    if op == "3":
        if itablo_adi == "":
            print("Sanatci bilgisi girilmedi.")
            continue  # Sanatçı bilgisi girilmediyse döngüye devam et
        else:
            sanatci.sarkileri_bastir()

    if op == "4":
        if itablo_adi == "":
            print("Sanatci bilgisi girilmedi.")
            continue  # Sanatçı bilgisi girilmediyse döngüye devam et
        else:
            output = sanatci.sarkileri_bastir()
            if output:
                sarki_ismi = input("Silinicek sarkinin ismini giriniz.")
                sanatci.sarki_sil(sarki_ismi)
                sanatci.sarkileri_bastir()
            else:
                continue
    if op == "5":
        if itablo_adi == "":
            print("Sanatci bilgisi girilmedi.")
            continue  # Sanatçı bilgisi girilmediyse döngüye devam et
        else:
            sanatci.toplam_sure()
