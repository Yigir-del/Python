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
