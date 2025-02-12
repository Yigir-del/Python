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
