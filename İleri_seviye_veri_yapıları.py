# Python'da Küme (set) Veri Yapısı

# Küme veri tipi sırasız ve değiştirilebilir bir koleksiyon olup, her öğe benzersizdir.
x = {1, 2, 3}
print(type(x))  # <class 'set'>

# Bir listeden küme oluşturulduğunda, tekrar eden öğeler tekilleştirilir.
liste = [1, 1, 2, 2, 3, 3]
print(set(liste))  # {1, 2, 3}

# Küme öğelerinin sırası belirsizdir.
for i in {"ahmet", "mehmet", "ayse"}:
    print(i)

# Küme işlemleri
x.add(6)       # Yeni bir eleman ekler (var olan bir eleman eklenemez).
x.discard(1)   # Belirtilen elemanı kümeden kaldırır (eleman yoksa hata vermez).
print(x)       # {2, 3, 6}

# Fark işlemi (difference): İlk kümede olup ikinci kümede olmayan elemanları döndürür.
kume1 = {10, 12, 13, 1, 2, 3}
kume2 = {10, 12, 13, 3, 4, 5}

print(kume1.difference(kume2))  # {1, 2}
print(kume2.difference(kume1))  # {4, 5}

# Güncellenmiş fark işlemi (difference_update): İlk kümede olup ikinci kümede olmayanları ilk kümeye atar.
kume1.difference_update(kume2)
print(kume1)  # {1, 2}

# Kesişim işlemi (intersection): Ortak elemanları döndürür.
kume1 = {10, 12, 13, 1, 2, 3}
kume2 = {10, 12, 13, 3, 4, 5}
print(kume1.intersection(kume2))  # {10, 12, 13, 3}

# Güncellenmiş kesişim işlemi (intersection_update): Ortak elemanları ilk kümeye atar.
kume1.intersection_update(kume2)
print(kume1)  # {10, 12, 13, 3}

# Ayrık kümeler mi? (isdisjoint): Ortak eleman olup olmadığını kontrol eder.
kume1 = {10, 12, 13, 1, 2, 3}
kume2 = {10, 12, 13, 3, 4, 5}
kume3 = {"ahmet", "mehmet", "ayse"}
print(kume1.isdisjoint(kume2))  # False (ortak eleman var)
print(kume1.isdisjoint(kume3))  # True  (ortak eleman yok)

# Diğer küme işlemleri:
kume1.issubset(kume2)  # Alt küme mi? (Tüm elemanları diğer kümede var mı?)
kume1.union(kume2)     # Birleşim kümesi (iki kümenin tüm elemanlarını içeren yeni bir küme döndürür).
kume1.update(kume2)    # Birleşim kümesini ilk kümeye atar.



# Sayısal işlemler
num = 100
print(num)         # 100 (Değişkenin kendisi)
print(bin(num))    # 0b1100100 (İkilik (binary) gösterimi)
print(hex(num))    # 0x64 (Onaltılık (hexadecimal) gösterimi)

num1 = -5
print(abs(num1))   # 5 (Mutlak değer)

print(round(3.5))  # 4 (Yuvarlama işlemi)
print(round(3.6))  # 4
print(round(3.4))  # 3

print(max(3, 4, 5, 6, -2, 34))  # 34 (En büyük değer)
print(min(3, 4, 5, 6, -2, 34))  # -2 (En küçük değer)

print(sum([3, 4, 5, 1, 4, 5]))  # 22 (Listedeki elemanların toplamı)

print(pow(2, 4))  # 16 (Üs alma: 2⁴)



# String işlemleri
string1 = "pyTHon"
print(string1)           # "pyTHon"
print(string1.upper())   # "PYTHON" (Tüm harfleri büyük yapar)
print(string1.lower())   # "python" (Tüm harfleri küçük yapar)

string2 = "Herkes ana baba baci gardas"
print(string2)                    # "Herkes ana baba baci gardas"
print(string2.replace("a", "o"))   # "Herkes ono bobo boci gordos" (Belirtilen karakterleri değiştirir)
print(string2.replace(" ", "-"))   # "Herkes-ana-baba-baci-gardas" (Boşlukları "-" ile değiştirir)

string3 = "Adana Demir Spor"
print(string3.startswith("Ad"))  # True (Belirtilen karakter dizisiyle başlıyor mu?)
print(string3.endswith("or"))    # True (Belirtilen karakter dizisiyle bitiyor mu?)

string4 = "Python programlama dili"
print(string4.split(" "))   # ['Python', 'programlama', 'dili'] (Boşluklara göre ayırır)
print(string4.strip("P"))   # "ython programlama dili" (Başta veya sonda belirtilen karakter varsa siler)
print(string4.lstrip("i"))  # "Python programlama dili" (Sondaki belirtilen karakteri siler)
print(string4.rstrip("i"))  # "Python programlama dil" (Baştaki belirtilen karakteri siler)
print(string4.count(" "))   # 2 (Belirtilen karakterin kaç kez geçtiğini bulur)
print(string4.find("o"))    # 4 (İlk geçen "o" karakterinin indeksini döndürür)
print(string4.find("z"))    # -1 (Bulamazsa -1 döndürür)
print(string4.rfind("o"))   # 17 (Sağdan başlayarak ilk geçen "o" karakterinin indeksini döndürür)



# Liste işlemleri
dizi = ["27", "01", "2005"]
print("/".join(dizi))  # "27/01/2005" (Liste elemanlarını belirtilen karakter ile birleştirir)

# Bir liste başlatma
my_list = [1, 2, 3, 4]

# Listeye bir eleman ekleme
my_list.append(6)

# İki yeni liste oluşturuluyor
list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 0, "sdf"]

# list1'i, list2'nin tüm elemanlarıyla genişletme
list1.extend(list2)
print(list1)  # list1'in, list2 ile genişledikten sonraki hâlini yazdırma

# list1'e, belirtilen indeks numarasına yeni bir eleman ekleme
list1.insert(2, "Python")
print(list1)  # list1'in, eleman ekleme işleminden sonraki hâlini yazdırma

# list1'den son elemanı çıkarma
list1.pop()
print(list1)  # list1'in, son elemanı çıkarıldıktan sonraki hâlini yazdırma

# list1'den belirli bir elemanı çıkarma
list1.remove("Python")
print(list1)  # list1'in, "Python" elemanı çıkarıldıktan sonraki hâlini yazdırma

# list1 içinde belirli bir elemanın ilk bulunduğu indeks numarasını bulma
print(list1.index(3))  # '3' elemanının listede bulunduğu indeks numarasını yazdırma

# list1'de belirli bir elemanın kaç kez tekrar ettiğini sayma
print(list1.count(1))  # '1' elemanının listede kaç kez geçtiğini yazdırma

# list1'i artan sıraya göre sıralama
list1.sort()
print(list1)  # list1'in artan sıraya göre sıralandıktan sonraki hâlini yazdırma

# list1'i azalan sıraya göre sıralama
list1.sort(reverse=True)
print(list1)  # list1'in azalan sıraya göre sıralandıktan sonraki hâlini yazdırma
