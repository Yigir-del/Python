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



#Açıklamaya üşeniyorum kendin çöz ne iş yaptıklarını 
num = 100
print(num)
print(bin(num))
print(hex(num))

num1 = -5
print(abs(num1))  #mutlak deger

print(round(3.5))
print(round(3.6))
print(round(3.4))

print(max(3,4,5,6,-2,34))
print(min(3,4,5,6,-2,34))

print(sum([3,4,5,1,4,5]))

print(pow(2,4)) #2**4



#Açıklamaya üşendiğim string ve dizi methodları.
string1 = "pyTHon"
print(string1)
print(string1.upper())
print(string1.lower())

string2 = "Herkes ana baba baci gardas"
print(string2)
print(string2.replace("a","o"))
print(string2.replace(" ","-"))

string3 = "Adana Demir Spor"
print(string3.startswith("Ad"))
print(string3.endswith("or"))

string4 = "Python programlama dili"
print(string4.split(" "))
print(string4.strip("P"))  #aradığın başta veya sondaysa siler
print(string4.lstrip("i")) #aradığın sondaysa siler
print(string4.rstrip("i")) #aradığın baştaysa siler
print(string4.count(" "))
print(string4.find("o"))
print(string4.find("z"))
print(string4.rfind("o"))

dizi = ["27","01","2005"]
print("/".join(dizi))



