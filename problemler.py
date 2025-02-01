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
                                               
    
