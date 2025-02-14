#map
def double(x):
    return x * 2
print(list(map(double,[1,2,3,4,5,5,6])))


#reduce
from functools import reduce
a = int(input("Bir sayi gir."))
list = range(1,a+1)
print(reduce(lambda x,y: x * y,list))


#filter
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

print(list((filter(asal_mi,range(1,100)))))


#zip
list1 = ["elif","nilgün","altuntas"]
list2 = ["yigit","efe","altuntas"]

print(list(zip(list1,list2)))

for i,j in zip(list2,list1):
    print(i,j)


#enumerate
liste = ["ahmet","bekir","izci","yigit"]
print(list(enumerate(liste)))

for index,isim in enumerate(liste):
    print(index,isim)


#all,any
liste = [False,False,False,False,True]
liste1 = [False,False,False,False,False]
liste2 = [True,True,True]
print(any(liste))
print(any(liste1))
print(any(liste2))
print(all(liste))
print(all(liste1))
print(all(liste2))


#Açıklamaya üşendiğim bazı şeyler daha
num = 100
print(num)
print(bin(num))
print(hex(num))

num1 = -5
print(abs(num1))  #mutlak deger

print(round(3.5))
print(round(3.6))
print(round(3.4))

print(max(3,4,5,6,-2,34))
print(min(3,4,5,6,-2,34))

print(sum([3,4,5,1,4,5]))

print(pow(2,4)) #2**4

