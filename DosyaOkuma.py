# Dosya İşlemleri: Açma, Yazma, Okuma

# Dosyayı açma ve yazma modları:
# "r" - Okuma modu: Dosyayı yalnızca okumak için açar. Dosya mevcut değilse hata verir.
# "w" - Yazma modu: Dosyayı yazmak için açar. Dosya varsa, içeriği siler ve yeni veri yazar.
# "r+" - Okuma ve yazma modu: Dosyayı hem okumak hem de yazmak için açar.
# "a" - Ekleme modu: Dosyanın sonuna veri ekler. Dosyadaki mevcut verileri silmeden devam eder.

# Dosyaya veri yazma:
with open("test", "w", encoding="UTF-8") as file:
    file.write("Mustafa Murat Coşkun\n")
    file.write("Yiğit efe altuntaş\n")
    file.write("Ameed\n")
    file.write("Beqo\n")
    file.write("İzci\n")

# Kullanıcıdan dosya adı alarak okuma işlemi:
try:
    a = input("Dosya adını giriniz: ")
    with open(a, "r", encoding="UTF-8") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("Dosya mevcut değil.")
finally:
    # Dosya otomatik olarak kapatılacak (with bloğu nedeniyle)
    pass

# Dosyadan veri okuma:
# Dosya okuma işlemi yapılırken, read() fonksiyonu ile tüm içerik okunabilir.
with open("test", "r", encoding="UTF-8") as file:
    print("1.")
    icerik = file.read()  # Tüm içeriği okur
    print(icerik)
    icerik2 = file.read()  # Okuma pointer'ı dosyanın sonuna geldiği için ikinci okuma boş döner
    print("2.")
    print(icerik2)

# Dosyadaki satır satır okuma işlemi:
with open("test", "r", encoding="UTF-8") as file:
    print("Readline")
    print(file.readline())  # İlk satır
    print(file.readline())  # İkinci satır
    print(file.readline())  # Üçüncü satır
    print(file.readline())  # Dördüncü satır

# Dosya pointer'ı üzerinde işlem yapmak (tell, seek):
with open("test", "r", encoding="UTF-8") as file:
    print(file.tell())  # Dosya pointer'ının bulunduğu konumu verir
    file.seek(20)  # Dosya pointer'ını 20. konuma taşır
    print(file.tell())  # Yeni konumu verir

    file.seek(5)  # 5. byte'a gider
    icerik = file.read(10)  # 10 byte okur
    print(icerik)
    print(file.tell())  # Son okuma sonrası pointer konumunu yazdırır

# Dosyaya veri yazma ve okuma:
with open("elif", "r+", encoding="UTF-8") as file2:
    file2.seek(10)  # Dosya pointer'ını 10. konuma taşır
    file2.write("deneme")  # Yazma işlemi

with open("elif", "r+", encoding="UTF-8") as file2:
    print(file2.read())  # Dosyanın içeriğini okur

# Dosyaya ekleme işlemi:
with open("test", "a", encoding="UTF-8") as file:
    file.write("Mert Erarslan\n")  # Dosyaya ekleme yapar

with open("test", "r+", encoding="UTF-8") as file:
    print(file.read())  # Dosya içeriğini okur

# Dosya içeriğini başa ekleme işlemi:
with open("test", "r+", encoding="UTF-8") as file:
    icerik = file.read()
    icerik = "Abdullah alrys\n" + icerik  # İçeriği başa ekler
    file.seek(0)  # Dosyanın başına geri döner
    print(icerik)

# Dosya içeriğini satır satır okuma ve düzenleme:
with open("test", "r+", encoding="UTF-8") as file:
    liste = file.readlines()  # Tüm satırları bir listeye alır
    print(liste)
    liste.insert(3, "Emrah karaduman\n")  # Listeye yeni bir satır ekler
    file.seek(0)  # Dosyanın başına döner
    for i in liste:
        file.write(i)  # Satırları dosyaya yazar
    file.seek(0)
    file.writelines(liste)  # Daha verimli yöntem ile listeyi yazma

# Not hesaplama ve dosyaya yazma:
def harf_hesapla(dizi):
    dizi = dizi[:-1]  # Satır sonu karakterini kaldır
    liste = dizi.split(",")  # Virgülle ayır
    ad = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    net = not1 * 1/10 + not2 * 3/10 + not3 * 6/10  # Ağırlıklı not hesaplama
    harf_notu = ""
    durum = ""
    # Durum belirleme
    if net >= 90:
        harf_notu = "AA"
        durum = "Geçer"
    elif net >= 80:
        harf_notu = "BA"
        durum = "Geçer"
    elif net >= 70:
        harf_notu = "BB"
        durum = "Geçer"
    elif net >= 60:
        harf_notu = "CB"
        durum = "Geçer"
    elif net >= 50:
        harf_notu = "CC"
        durum = "Geçer"
    elif net >= 45:
        harf_notu = "DC"
        durum = "Kalır"
    elif net >= 40:
        harf_notu = "DD"
        durum = "Kalır"
    else:
        harf_notu = "FF"
        durum = "Kalır"

    return ad + "--------------->" + harf_notu + " " + durum + "\n"

# Dosyadaki öğrenci notlarını işleyip dosyaya yazma:
list1 = []
with open("dosya.txt", "r", encoding="utf-8") as file:
    for i in file:
        list1.append(harf_hesapla(i))  # Her satır için harf notu hesaplanır

with open("harf_notlari", "w", encoding="utf-8") as file2:
    file2.writelines(list1)  # Harf notlarını yazma

# Geçen ve kalanları ayrı dosyaya yazma:
with open("harf_notlari", "r", encoding="utf-8") as file3:
    with open("kalanlar", "w", encoding="utf-8") as file4:
        for k in file3:
            if "Kalır" in k:
                k = k[:-6]  # "Kalır" kelimesini siler
                list2.append(k)
                file4.writelines(list2)  # Kalanları yazma

with open("harf_notlari", "r", encoding="utf-8") as file3:
    with open("gecenler", "w", encoding="utf-8") as file4:
        for j in file3:
            if "Geçer" in j:
                j = j[:-6]  # "Geçer" kelimesini siler
                list2.append(j)
                file4.writelines(list2)  # Geçenleri yazma

# Futbolcu isimlerini kulüplere göre ayırma:
liste1 = []
liste2 = []
liste3 = []

def esle(dizi):
    dizi = dizi[:-1]  # Satır sonu karakterini kaldır
    liste = dizi.split(",")  # Virgülle ayır
    takim = liste[1].strip()  # Kulüp ismini al ve boşluklardan kurtul
    futbolcu = liste[0].strip()  # Futbolcu ismini al ve boşluklardan kurtul
    if takim == "Galatasaray":
        liste1.append(futbolcu + "\n")
    elif takim == "Fenerbahçe":
        liste2.append(futbolcu + "\n")
    elif takim == "Beşiktaş":
        liste3.append(futbolcu + "\n")

with open("Futbolcular.txt", "r", encoding="utf-8") as file:
    for i in file:
        esle(i)  # Futbolcuları kulüplerine göre ayırma

# Kulüplerin futbolcu listesini dosyaya yazma:
with open("Galatasaray.txt", "w", encoding="utf-8") as file2:
    file2.writelines(liste1)

with open("Fenerbahçe.txt", "w", encoding="utf-8") as file3:
    file3.writelines(liste2)

with open("Beşiktaş.txt", "w", encoding="utf-8") as file4:
    file4.writelines(liste3)
