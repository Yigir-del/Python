Matematiksel ifadeler/
Diğer programlama dillerinde olandan çokda farklı kurallara sahip değil her şey neredeyse aynı birkaç küçük farktan bahsedicem.

-> 10//3 == 3
-> 5**3 == 125
Bu kadar

Stringler/
Kelimelere cümlelere string deriz.
"ahmet"
'ahmet'
2 gösterimde uygundur.

'Güzide' nin evi' -> hata verir çünkü ilk kesme işaretini bitirici '  sanar.
'Güzide\' nin evi' -> hata vermez çünkü python da ( \ slash ) karakteri kaçış karakteridir.
Kaçış karakterini daha detaylı anlatıcam.

\\: Ters eğik çizgi \
\': Tek tırnak işareti '
\": Çift tırnak işareti "
\n: Yeni satır (newline)
\t: Sekme (tab)
\r: Satır başı (carriage return)
\b: Geri alma (backspace)
\f: Form besleme (form feed)
\v: Dikey sekme (vertical tab)


Lan bide değişken tanımlayıp içine değer atamak çok kolay değişken tanımlamak diye bir şey bile yok.

-> AD = "Tuğçe"
-> AD1 = "Yiğit"
Bu kadar

-> AD + AD1 == TuğçeYiğit
-> AD * 3 == TuğçeTuğçeTuğçe
Bu ne lan çok kolay.


Print/
Lan bu fonksiyon çok güçlü her şeyi sorunsuz bastırıyo.

-> print("merhaba") == merhaba
-> print("merhaba","tuğçe") == merhaba tuğçe
-> print("merhaba",5) == merhaba 5"

-> print("merhaba" + 5) == hata verir (e biz zahmet)
-> print("merhaba" + str(5)) == merhaba5
str() == stringe çevirme fonksiyonu.
-> print("5" + 8) == hata verir
-> print(int("5) + 8) == hata vermez
int() == integere çevirme fonksiyonu.
-> print("5.5" + 5) == hata verir
-> print(int("5.5") + 5) == hata verir
-> print(float("5.5") + 5) == hata vermez
float() == floata çevirme fonksiyonu.

print("""ahmet
mehmet
yiğit""") 
bu kod hatasız çalışır.

Diyelim ki 
-> a = "yazilim"
-> print(a[3:]) == ilim
-> print(len(a)) == 7
piton güzel şey.


/*
print("Oyuncu kaydetme programi:")
ad = input("Ad: ")
soyad = input("soyad: ")
takim = input("takim: ")

oyuncu = [ad,soyad,takim]
print("Oyuncunun adi:{} \n Oyuncunun soyadi:{} \n oyuncunun oynadiği takim:{} ".format(oyuncu[0],oyuncu[1],oyuncu[2]))
*/





