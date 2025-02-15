# Armstrong Sayısı Kontrol Programı

def is_armstrong(number: int) -> bool:
    """Verilen sayının Armstrong sayısı olup olmadığını kontrol eder."""
    str_num = str(number)
    return sum(int(digit) ** len(str_num) for digit in str_num) == number

number = int(input("Bir sayı giriniz: "))
if is_armstrong(number):
    print(f"{number} bir Armstrong sayısıdır.")
else:
    print(f"{number} bir Armstrong sayısı değildir.")

# Çarpım Tablosu

def print_multiplication_table():
    """1-10 arasındaki sayıların çarpım tablosunu ekrana yazdırır."""
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{j} x {i} = {i * j}".ljust(12), end=" ")
            if j == 5:
                print(" ")  # İlk 5 sütundan sonra boşluk bırak
        print()

print("\nÇarpım Tablosu Programı\n")
print_multiplication_table()

# Kullanıcıdan Sayı Alarak Toplama İşlemi

def sum_input_numbers():
    """Kullanıcı tarafından girilen sayıları toplar, çıkmak için 'q' kullanılabilir."""
    total = 0
    while True:
        user_input = input("Sayı giriniz (çıkmak için q): ")
        if user_input.lower() == "q":
            print(f"Toplam: {total}")
            break
        total += int(user_input)

sum_input_numbers()

# 3'e Tam Bölünen Sayıları Bulma

def find_divisible_by_three(limit: int) -> list:
    """Belirtilen limit içinde 3'e tam bölünen sayıları döndürür."""
    return [num for num in range(1, limit) if num % 3 == 0]

print("\n3'e tam bölünen sayılar:")
print(find_divisible_by_three(100))

# Asal Sayı Kontrolü

def is_prime(number: int) -> bool:
    """Verilen sayının asal olup olmadığını kontrol eder."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print("\nAsal Sayı Testi")
print(is_prime(100))
print(is_prime(7))
print(is_prime(1))

# Bir Sayının Tam Bölenlerini Bulma

def find_divisors(number: int) -> list:
    """Verilen sayının tam bölenlerini bulur."""
    return [i for i in range(1, number + 1) if number % i == 0]

print("\nTam Bölenler:")
print(find_divisors(100))
print(find_divisors(99))

# Mükemmel Sayıları Bulma

def find_perfect_numbers(limit: int) -> list:
    """Belirtilen limit içerisindeki mükemmel sayıları bulur."""
    return [num for num in range(1, limit) if sum(find_divisors(num)[:-1]) == num]

print("\n1'den 1000'e kadar olan mükemmel sayılar:")
print(find_perfect_numbers(1000))

# EBOB Hesaplama

def calculate_gcd(a: int, b: int) -> int:
    """İki sayının en büyük ortak bölenini (EBOB) hesaplar."""
    while b:
        a, b = b, a % b
    return a

print("\nEBOB Hesaplama")
print(calculate_gcd(140, 91))

# EKOK Hesaplama

def calculate_lcm(a: int, b: int) -> int:
    """İki sayının en küçük ortak katını (EKOK) hesaplar."""
    return (a * b) // calculate_gcd(a, b)

print("\nEKOK Hesaplama")
print(calculate_lcm(140, 91))

# Pisagor Üçgeni Bulma

def find_pythagorean_triples(limit: int):
    """Belirtilen limit içinde Pisagor üçgenlerini bulur."""
    for a in range(1, limit):
        for b in range(a, limit):
            c = (a ** 2 + b ** 2) ** 0.5
            if c.is_integer():
                print(f"{a}, {b}, {int(c)}")

print("\nPisagor Üçgenleri")
find_pythagorean_triples(100)

# Alan Hesaplama

def calculate_area(dimensions: tuple) -> int:
    """Bir dikdörtgenin alanını hesaplar."""
    return dimensions[0] * dimensions[1]

print("\nDikdörtgen Alanları")
shapes = [(3, 4), (10, 3), (5, 6), (1, 9)]
print(list(map(calculate_area, shapes)))

# Üçgen Olup Olmadığını Kontrol Etme

def is_triangle(sides: tuple) -> bool:
    """Verilen kenar uzunlukları ile üçgen oluşturulup oluşturulamayacağını kontrol eder."""
    a, b, c = sorted(sides)
    return a + b > c

print("\nÜçgen Olma Testi")
triangles = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]
print(list(filter(is_triangle, triangles)))

# Çift Sayıları Toplama
from functools import reduce

def sum_even_numbers(numbers: list) -> int:
    """Verilen sayı listesindeki çift sayıların toplamını döndürür."""
    return reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, numbers))

print("\nÇift Sayıların Toplamı")
print(sum_even_numbers(list(range(1, 11))))

# Ad-Soyad Eşleştirme

def match_names(names: list, surnames: list):
    """İsim ve soyisimleri eşleştirerek çıktı olarak verir."""
    return list(zip(names, surnames))

print("\nAd-Soyad Eşleşmeleri")
names = ["Kerim", "Tarik", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
surnames = ["Yilmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]
print(match_names(names, surnames))


#Frenkans hesaplama.
class Dizi:
    def __init__(self, dizgi):
        self.dizgi = dizgi
    
    def frekans(self):
        harf_dict = dict()
        for i in self.dizgi:
            if i in harf_dict:
                harf_dict[i] = str(int(harf_dict[i]) + 1)
            else:
                harf_dict[i] = "1"
        for i, j in harf_dict.items():
            print("{} -> {}".format(i, j))

# Sınıf örneği oluşturulup metot çağrılır
dizi = Dizi("ProgramlamaOdeviileriSeviyeVeriYapilariveObjeleripynb")
dizi.frekans()


#Baş harf birleştirme
with open("siir.txt","r",encoding="utf-8") as file:
    dize_liste = list()
    bas_harf_liste = list()
    for satir in file:
        satir = satir.strip()
        dize_liste.append(satir)

    for i in dize_liste:
        bas_harf_liste.append(i[0])
    bas_harf_liste = "".join(bas_harf_liste)
    print(bas_harf_liste)



def mail_test(mail_list):
    true_mail_extensions = [".com",".net",".org",".edu",".gov",".co.uk",".io",".us",".de",".fr",".tr",".xyz",".info",".biz",".online",".me"]

    true_mail = list()
    false_mail = list()


    for mail in mail_list:
        mail = mail.strip()

        if "@" in mail:
            domain_part = mail.split("@")[-1]

            if any(domain_part.endswith(ext) for ext in true_mail_extensions):
                true_mail.append(mail)
            else:
                false_mail.append(mail)

        else:
            false_mail.append(mail)
        
    print("""True mails
          {} -> {} tane
          """.format(true_mail,len(true_mail)))
    
    print("""False mails
          {} -> {} tane
          """.format(false_mail,len(false_mail)))

with open("mailler.txt","r",encoding="utf-8") as file:
    mails = [line.strip() for line in file]

mail_test(mails)



isims = ["Kerim","Tarik","Ezgi","Kemal","Ilkay","Sukran","Merve"]
soyisim = ["Yilmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

full_name = dict(zip(isims,soyisim))
sorted_full_name = list()

isims = sorted(isims)

sorted_full_name = [isim + full_name[isim] for isim in isims] 

print(sorted_full_name)


