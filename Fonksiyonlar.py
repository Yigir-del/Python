# map Fonksiyonu:
# "map" fonksiyonu, verilen bir fonksiyonu bir iterable (tekrarlanabilir) üzerindeki her öğe için uygular.
# Bu örnekte, her öğe için iki katını alan bir fonksiyon kullanılmıştır.

def double(x):
    return x * 2

# Listede her öğenin iki katı alınır ve sonuç bir liste olarak yazdırılır.
print(list(map(double, [1, 2, 3, 4, 5, 5, 6])))


# reduce Fonksiyonu:
# "reduce" fonksiyonu, bir iterabl içindeki öğeleri, verilen iki parametreli bir fonksiyonla sırasıyla birleştirir.
# Örneğin, bu fonksiyonla bir sayı aralığındaki sayıların çarpımını hesaplıyoruz.

from functools import reduce

# Kullanıcıdan pozitif bir tam sayı alınır.
a = int(input("Bir sayı giriniz: "))

# 1'den kullanıcı tarafından girilen sayıya kadar olan tam sayılar oluşturulur.
num_list = range(1, a + 1)

# Liste elemanlarının çarpımı hesaplanır ve yazdırılır.
print(reduce(lambda x, y: x * y, num_list))


# filter Fonksiyonu:
# "filter" fonksiyonu, verilen bir fonksiyonu, bir iterable üzerindeki her öğeye uygular ve 
# True dönen öğeleri filtreleyerek döndürür. Aşağıdaki örnekte asal sayılar filtrelenmektedir.

def asal_mi(sayi):
    if sayi == 1:
        return False
    elif sayi == 2:
        return True
    elif sayi > 2:
        i = 2
        while i < sayi:
            if sayi % i == 0:
                return False
            i += 1      
        return True

# 1'den 100'e kadar olan asal sayılar filtrelenir ve yazdırılır.
print(list(filter(asal_mi, range(1, 100))))


# zip Fonksiyonu:
# "zip" fonksiyonu, iki veya daha fazla iterable'ı birleştirir ve her iterable'dan birer öğe alarak
# bir tuple oluşturur. Sonuç, bir liste şeklinde döndürülür.

list1 = ["elif", "nilgün", "altuntas"]
list2 = ["yigit", "efe", "altuntas"]

# list1 ve list2'yi zipler ve her bir öğeyi tuple olarak yazdırır.
print(list(zip(list1, list2)))

# zip işlemi ile birleştirilmiş iki listeyi döngüde yazdırır.
for i, j in zip(list2, list1):
    print(i, j)


# enumerate Fonksiyonu:
# "enumerate" fonksiyonu, bir iterable'a karşılık gelen index ve öğe çiftlerini döndüren bir fonksiyondur.
# Bu sayede her bir öğenin dizindeki konumu ile birlikte kullanılabilir.

liste = ["ahmet", "bekir", "izci", "yigit"]

# Listeyi enumerate ile alır ve index + öğe çiftlerini yazdırır.
print(list(enumerate(liste)))

# enumerate fonksiyonu ile öğelerin index ve değerini döngüde yazdırır.
for index, isim in enumerate(liste):
    print(index, isim)


# all ve any Fonksiyonları:
# "all" fonksiyonu, tüm öğelerin True olup olmadığını kontrol eder, eğer tüm öğeler True ise True döner.
# "any" fonksiyonu ise, en az bir öğe True ise True döner.

liste = [False, False, False, False, True]
liste1 = [False, False, False, False, False]
liste2 = [True, True, True]

# any ve all fonksiyonlarının örnek kullanımları.
print(any(liste))     # Liste içinde en az bir True var mı?
print(any(liste1))    # Liste içinde en az bir True var mı?
print(any(liste2))    # Liste içinde en az bir True var mı?
print(all(liste))     # Liste içindeki tüm öğeler True mu?
print(all(liste1))    # Liste içindeki tüm öğeler True mu?
print(all(liste2))    # Liste içindeki tüm öğeler True mu?
