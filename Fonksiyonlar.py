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







                    ***************************************************DECORATORLAR***************************************************
Brain dmg %100
                    
def my_decorator(func):
    def wrapper(iter):
        mukemmeller = []
        for sayi in iter:
            if 0 < sayi < 2:
                continue
            if sayi >= 2:
                bolenler = [i for i in range(1,sayi//2 + 1) if sayi % i == 0]
                if sum(bolenler) == sayi:
                    mukemmeller.append(sayi)
        print(f"{mukemmeller} sayilari mukemmel sayilardir range: {len(iter)}")
        asal_sayilar = func(iter)
        return f"{asal_sayilar} sayilari asal sayilardir range: {len(iter)}"
    return wrapper 

@my_decorator
def asal_bul(iter):
    asallar = []
    for sayi in iter:
        if 0 < sayi < 2:
            continue
        if sayi >= 2:
            sorgu = [sayi % i == 0 for i in range(2,int(sayi**0.5) + 1)]
            if not any(sorgu):
                asallar.append(sayi)
    return asallar

print(asal_bul(range(1000)))




                    ***************************************************Iteratorlar***************************************************

class My_iter:
    def __init__(self,limit):
        self.limit = limit
        self.s1 = 1
        self.s2 = 1
        self.count = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count <= self.limit:
            if self.count == 1 or self.count == 2:
                self.count += 1
                return self.s1
            else:
                    toplam = self.s1 + self.s2
                    self.s1 = self.s2
                    self.s2 = toplam
                    self.count += 1
                    return toplam
        else:
            raise StopIteration

iter = My_iter(10)
for i in iter:
    print(i)
print(next(iter))




class Kareler:
    def __init__(self,max):
        self.max = max
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.max:
            self.counter += 1   
            return self.counter ** 2
        else:
            raise StopIteration

kareler = Kareler(5)
for i in kareler:
    print(i)



class Asallar():
    def __init__(self):
        self.sayi = 2  # Başlangıç olarak 2'yi alıyoruz (ilk asal sayı)
    
    def __iter__(self):
        return self

    def __next__(self):
        while self.sayi < 1000:
            # Asal sayıları kontrol etmek için 2 ile sayının karekökü arasındaki sayılarla modülüs alıyoruz
            sorgu = (self.sayi % i == 0 for i in range(2, int(self.sayi ** 0.5) + 1))
            if not any(sorgu):  # Eğer sayı asal ise
                sonuc = self.sayi
                self.sayi += 1
                return sonuc
            self.sayi += 1  # Eğer asal değilse bir sonraki sayıyı kontrol et
        raise StopIteration

asal = Asallar()
for i in asal:
    print(i)

                        
