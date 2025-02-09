import random
import time

class Bilgisayar:
    def __init__(self, pc_durum="kapali", ses=0, uygulamalar=["hesap_makinesi", "kelime_tahmin", "sayi_tahmin"]):
        self.pc_durum = pc_durum
        self.ses = ses
        self.uygulamalar = uygulamalar
    def __str__(self):
        print("Genel bilgisayar denemesi")

    def pc_ac(self):
        time.sleep(1)
        if self.pc_durum == "acik":
            print("pc zaten acik.")
            return
        else:
            self.pc_durum = "acik"
            print("pc acildi.")

    def pc_kapat(self):
        time.sleep(1)
        if self.pc_durum == "kapali":
            print("pc zaten kapali.")
            return
        else:
            self.pc_durum = "kapali"
            print("pc kapatildi.")

    def ses_kontrol(self):
        op = input("Sesi yukseltmek icin: '>'\tSesi kismak icin: '<'  cikmak icin 'q'")
        if op == '<':
            if self.ses != 0:
                self.ses -= 1
                print("Ses seviyesi: {}".format(self.ses))
        elif op == '>':
            if self.ses != 100:
                self.ses += 1
                print("Ses seviyesi: {}".format(self.ses))
        elif op == "q":
            return
        else:
            print("Hatali giris.")

    def bastir(self):
        print("""
        Hesap makinesi icin -> 1
        Kelime oyunu icin   -> 2
        Sayi oyunu icin     -> 3        
        """)


    def hesap_makinesi(self):
        print("Hesap makinesine hos geldiniz.")
        giris = input("Lutfen virgül(,) ile ayirarak bir sayi bir operator(*,-,/,+) ve ikinci sayiyi giriniz. ex(10,*,20 = 200) çikmak icin 'q'")
        list1 = giris.split(",")
        if list1 == 'q':
            return
        if len(list1) == 3:
            if list1[1] == '+':
                print("{} {} {} = {}".format(list1[0], list1[1], list1[2], int(list1[0]) + int(list1[2])))
            elif list1[1] == '-':
                print("{} {} {} = {}".format(list1[0], list1[1], list1[2], int(list1[0]) - int(list1[2])))
            elif list1[1] == '*':
                print("{} {} {} = {}".format(list1[0], list1[1], list1[2], int(list1[0]) * int(list1[2])))
            elif list1[1] == '/':
                print("{} {} {} = {}".format(list1[0], list1[1], list1[2], int(list1[0]) / int(list1[2])))
            else:
                print("Hatali giris.")

    def kelime_tahmin(self):
        print("Kelime tahmini oyununa hos geldin.")
        kelime_listesi = ["ilkin", "mustafa", "yigit", "yavuz", "elif","ahmet","bekir","izci","akbar"]
        random_sayi = random.randint(0, len(kelime_listesi)-1)
        secilen_kelime = kelime_listesi[random_sayi]
        oyun_list = ["_" for _ in range(len(secilen_kelime))]
        kalp = 10
        while True:
            counter = 0
            print(oyun_list)
            harf = input("Bir harf giriniz.(çikmak icin 'q')")
            if harf == 'q':
                break

            elif harf in secilen_kelime:
                for i in secilen_kelime:
                    if harf == i:
                        oyun_list[counter] = harf
                        counter += 1
                    else:
                        counter += 1
            else:
                if kalp == 0:
                    print("Kaybettin! Kalp = {}".format(kalp))
                    print(secilen_kelime)
                    break
                print("Kalp = {}".format(kalp))
                kalp -= 1
            if not('_' in oyun_list):
                print("Tebrikler! Kazandin  Kalp = {}".format(kalp))
                print(oyun_list)
                break

    def sayi_tahmin(self):
        print("Sayi tahmin oyununa hosgeldin.")
        sayi = random.randint(1, 1000)
        while True:
            tahmin = input("Bir sayi giriniz.")
            if tahmin < sayi:
                print("Daha buyuk.")
            elif tahmin > sayi:
                print("Daha kucuk.")
            elif tahmin == sayi:
                print("Tebrikler! Dogru cevap.")

bilgisayar = Bilgisayar()
print("Bilgisayara hosgeldiniz.")
print("""
    Bilgisayari acmak icin     -> 1
    Bilgisayari kapatmak icin  -> 2
    Ses ayarlari icin          -> 3 
    Uygulamalar icin           -> 4
    Çikmak icin                ->'q'
    """)
durum = False
while True:
    if durum:
        print("Ana menuye hosgeldiniz.")
    istek = input()
    if istek == 'q':
        break
    if istek == "1":
        print("Bilgisayar aciliyor...")
        bilgisayar.pc_ac()
        durum = True
    if istek == "2":
        if not durum:
            print("Bilgisayar kapaliyken bu islem gerceklestirilemez.")
        if durum:
            print("Bilgisayar kapatiliyor...")
            bilgisayar.pc_kapat()
            durum = False
    if istek == "3":
        if not durum:
            print("Bilgisayar kapaliyken bu islem gerceklestirilemez.")

        if durum:
            print("Ses ayarlarina giriliyor...")
            bilgisayar.ses_kontrol()
    if istek == "4":
        if not durum:
            print("Bilgisayar kapaliyken bu islem gerceklestirilemez.")
        
        if durum:
            print("Uygulamalara giriliyor...")
            bilgisayar.bastir()
            istek2 = input()
            if istek2 == "1":
                bilgisayar.hesap_makinesi()
            elif istek2 == "2":
                bilgisayar.kelime_tahmin()
            elif istek2 == "3":
                bilgisayar.sayi_tahmin()
            else:
                print("Gecersiz giris.")
