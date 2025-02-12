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



