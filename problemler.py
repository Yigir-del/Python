print("Armstrong sayısı programı.")

x = input("Bir sayı giriniz: ")
list1 = [int(a)**len(x) for a in x]
sumlist = sum(list1)
if sumlist == int(x):
    print(f"{x} sayısı bir armstrong sayısıdır.")
else:
    print(f"{x} sayısı bir armstrong sayısı değildir. {sumlist}")



print("Çarpım Tablosu Programı\n")

for i in range(1, 11):  # 1'den 10'a kadar
    for k in range(1, 6):  # İlk 5 sütun
        print(f"{k} x {i} = {i*k}".ljust(12), end=" ")  # Sabit genişlikte hizala
    print()  # Her satırdan sonra alt satıra geç

print()  # İki tabloyu ayırmak için boşluk

for i in range(1, 11):  # 1'den 10'a kadar
    for k in range(6, 11):  # 6-10 arasındaki sütunlar
        print(f"{k} x {i} = {i*k}".ljust(12), end=" ")  
    print()  


print("İstenilen sayıları toplayan program.")

counter = 0
while True:
    x = input("Sayı giriniz (çıkmak için q): ")
    if x == "q":
        print("Toplam {}".format(counter))
        break
    counter += int(x)




print("3'e tam bölünen sayıları bulan program.")

list1 = [i for i in range(1,100) if i % 3 == 0]
print(list1)



print("Asal sayı bulma.")

def asalfonk(num):
    if num == 1:
        return False
    elif num < 1:
        return print("Error")
    else:
        list2 = [i for i in range(2,num) if num % i == 0]
        if len(list2) == 0:
            return True
        else:
            return False

print(asalfonk(100))
print(asalfonk(1))
print(asalfonk(-5))
print(asalfonk(100001))




print("Tam bölen bulma.")

def tambolenfonk(num):
    if num == 1:
        return False
    elif num < 1:
        return print("Error")
    else:
        list2 = [i for i in range(2,num) if num % i == 0]
        if len(list2) == 0:
            print("{} Sayısı bir asal sayıdır.".format(num))
        else:
            print(list2)

tambolenfonk(100)
tambolenfonk(99)
tambolenfonk(-10)




print("1 den 1000 e mükemmel sayılar.")

def mukemmel():
    list1 = []
    for i in range(1,1000):
        list2 = [k for k in range(1,(i//2)+1) if i % k == 0]
        if sum(list2) == i:
            list1.append(i)
    print(list1)

mukemmel()



import math

print("En büyük ortak bölen.")

def Ebob(num1,num2):
    list1 = [i for i in range(1, num1//2+1) if num1 % i == 0]
    list2 = [k for k in range(1, num2//2+1) if num2 % k == 0]
    list3 = [x for x in list1 if x in list2]
    ebob = max(list3)
    print(ebob)
Ebob(140,91)





import math

print("En küçük ortak kat.")

def ekoks(num1,num2):
    list1 = [i for i in range(1, num1//2+1) if num1 % i == 0]
    list2 = [k for k in range(1, num2//2+1) if num2 % k == 0]
    list3 = [x for x in list1 if x in list2]
    ebob = max(list3)
    print(num1*num2 / ebob)
ekoks(140,91)





print("Pisagor üçgeni testi.")

def pisagor():
    for i in range(1,101):
        for k in range(1,101):
            hipotenus = (i**2 + k**2)**0.5
            if hipotenus in range(1,101):
                print("{} + {} = {}".format(k,i,hipotenus))
pisagor()


print("Alan hesap")
def alan_hesap(liste):
    return liste[0] * liste[1]

kenarlar = [(3,4),(10,3),(5,6),(1,9)]
print(list(map(alan_hesap,kenarlar)))


print("Ucgen olma testi")
liste = [(3,4,5),(6,8,10),(3,10,7)]
def ucgen_testi(tup):
    if tup[0] + tup[1] > tup[2]:
        if tup[1] + tup[2] > tup[0]:
            if tup[2] + tup[0] > tup[1]:
                return True
    return False
print(list(filter(ucgen_testi,liste)))


print("Cift sayilari toplayan fonksiyon")
from functools import reduce
liste = range(1,11)

cift = list(filter(lambda x : x % 2 == 0,liste))
print(reduce(lambda x,y: x+y,cift))
