print("Armstrong sayısı programı.")

x = input("Bir sayı giriniz: ")
list1 = [int(a)**len(x) for a in x]
sumlist = sum(list1)
if sumlist == int(x):
    print(f"{x} sayısı bir armstrong sayısıdır.")
else:
    print(f"{x} sayısı bir armstrong sayısı değildir. {sumlist}")
