file = open("file_name","mode",encoding)  
MODE/
"r": Dosyayı sadece okuma modunda açar. file.read() ile dosyayı okuyabilirsiniz.
"w": Dosyayı yazma modunda açar. Eğer dosya zaten varsa, içeriği siler ve yeni içerik yazar. file.write() ile dosyaya yazabilirsiniz.
"r+": Hem okuma hem yazma modunda açar. file.read() ile dosyayı okuyabilir ve file.write() ile dosyaya yazabilirsiniz.
"a": Dosyayı ekleme modunda açar. Dosyanın sonuna veri ekler (mevcut verileri silmeden). file.write() ile ekleme yapabilirsiniz.
/


file = open("test","w",encoding= "UTF - 8")
file.write("Mustafa Murat Coşkun\n")
file.write("Yiğit efe altuntaş\n")
file.write("Ameed\n")
file.write("Beqo\n")
file.write("İzci\n")

try:
    a = input()
    file = open(a,"r",encoding= "UTF-8")
    for i in file:
        print(i,end="")
except FileNotFoundError:
    print("Dosya mevcut degil")
finally:
    file.close()



file = open("test","r",encoding="UTF-8")
print("1.")
icerik = file.read()
print(icerik)
icerik2 = file.read()
print("2.")
print(icerik2)

file = open("test","r",encoding="UTF-8")
print("Readline")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


with open("test","r",encoding= "UTF - 8") as file:
    print(file.tell())
    file.seek(20)
    print(file.tell())

    file.seek(5)
    icerik = file.read(10)
    print(icerik)
    print(file.tell())
print("------------------------------------------------------------------------")

with open("elif","r+",encoding="UTF - 8") as file2:
    file2.seek(10)
    file2.write("deneme")
with open("elif","r+",encoding="UTF - 8") as file2:
    print(file2.read())

print("------------------------------------------------------------------------")

with open("test","a",encoding="UTF-8") as file:
    file.write("Mert Erarslan\n")
with open("test","r+",encoding= "utf-8") as file:
    print(file.read())

print("------------------------------------------------------------------------")

with open("test","r+",encoding="utf-8") as file:
    icerik = file.read()
    icerik = "Abdullah alrys\n" + icerik
    file.seek(0)
    print(icerik)


print("------------------------------------------------------------------------")

with open("test","r+",encoding="utf-8") as file:
    liste = file.readlines()
    print(liste)
    liste.insert(3,"Emrah karaduman\n")
    file.seek(0)
    for i in liste:
        file.write(i)
    file.seek(0)
    "for döngüsü yerine"
    file.writelines(liste)
with open("test","r+",encoding="utf-8") as file:
    print(file.read())








def harf_hesapla(dizi):
    dizi = dizi[:-1]
    liste = dizi.split(",")
    ad = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    net = not1 * 1/10 + not2 * 3/10 + not3 * 6/10
    harf_notu = ""
    durum = ""
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
        durum = "Kalir"
    elif net >= 40:
        harf_notu = "DD"
        durum = "Kalir"
    else:
        harf_notu = "FF"
        durum = "Kalir"

    if durum == "Geçer":
        return ad + "--------------->" + harf_notu + " " + durum + "\n"
    elif durum == "Kalir":
        return ad + "--------------->" + harf_notu + " " + durum + "\n"
    
list1 = []
list2 = []
list3 = []
with open("dosya.txt","r",encoding="utf-8") as file:
    for i in file:
        list1.append(harf_hesapla(i))
with open("harf_notlari","w",encoding="utf-8") as file2:
    file2.writelines(list1)
with open("harf_notlari","r",encoding="utf-8") as file3:
    with open("kalanlar","w",encoding="utf-8") as file4:
        for k in file3:
            if "Kalir" in k:
                k = k[:-6]
                k += "\n"
                list2.append(k)
                file4.writelines(list2)

with open("harf_notlari","r",encoding="utf-8") as file3:
    with open("gecenler","w",encoding="utf-8") as file4:
        for j in file3:
            if "Geçer" in j:
                j = j[:-6]
                j += "\n"
                list2.append(j)
                file4.writelines(list2)
            
    




liste1 = []
liste2 = []
liste3 = []

def esle(dizi):
    dizi = dizi[:-1]  # Satır sonu karakterini kaldır
    liste = dizi.split(",")
    takim = liste[1].strip()  # Boşluklardan kurtul
    futbolcu = liste[0].strip()  # Boşluklardan kurtul
    if takim == "Galatasaray":
        liste1.append(futbolcu + "\n")
    elif takim == "Fenerbahçe":
        liste2.append(futbolcu + "\n")
    elif takim == "Beşiktaş":
        liste3.append(futbolcu + "\n")

with open("Futbolcular.txt", "r", encoding="utf-8") as file:
    for i in file:
        esle(i)

with open("Galatasaray.txt", "w", encoding="utf-8") as file2:
    file2.writelines(liste1)

with open("Fenerbahçe.txt", "w", encoding="utf-8") as file3:
    file3.writelines(liste2)

with open("Beşiktaş.txt", "w", encoding="utf-8") as file4:
    file4.writelines(liste3)









