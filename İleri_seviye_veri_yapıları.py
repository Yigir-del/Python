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

