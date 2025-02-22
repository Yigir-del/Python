******************************************************************DateTime*********************************************************************************

from datetime import datetime, timedelta

# Şu anki zamanı al
now = datetime.now()
print("Şu anki tarih ve saat:", now)
print("Yıl:", now.year)
print("Ay:", now.month)
print("Gün:", now.day)
print("Saat:", now.hour)
print("Dakika:", now.minute)
print("Saniye:", now.second)
print("Mikrosaniye:", now.microsecond)

# Ctime formatında gösterim
print("Ctime formatında:", datetime.ctime(now))

# Özel formatlama
print("Yıl (YYYY formatında):", datetime.strftime(now, "%Y"))
print("Tarih (GG-AA-YYYY):", datetime.strftime(now, "%d-%m-%Y"))
print("Saat (HH:MM:SS):", datetime.strftime(now, "%H:%M:%S"))

# Belirli bir tarih oluşturma
tarih = datetime(1970, 1, 1)
print("Belirli bir tarih:", tarih)

# İki tarih arasındaki fark
su_an = datetime.now()
fark = su_an - tarih
print("1970'ten bugüne geçen süre:", fark)
print("Toplam gün:", fark.days)
print("Toplam saniye:", fark.total_seconds())

# Zaman ekleme ve çıkarma
bir_hafta_sonra = now + timedelta(days=7)
print("Bir hafta sonraki tarih:", bir_hafta_sonra)

bir_gun_once = now - timedelta(days=1)
print("Bir gün önceki tarih:", bir_gun_once)

# Belirli bir tarihi parse etme
tarih_str = "2025-02-22 15:30:00"
parsed_tarih = datetime.strptime(tarih_str, "%Y-%m-%d %H:%M:%S")
print("Parse edilen tarih:", parsed_tarih)


******************************************************************OS*********************************************************************************
import os
from datetime import datetime

# Geçerli çalışma dizinini al
print("Geçerli Dizin:", os.getcwd())

# Dizin içeriğini listele
print("Dizin İçeriği:")
for i in os.listdir():
    print(i)

# Yeni klasör oluşturma
# os.mkdir("DenemeOs")
# os.makedirs("Deneme2/Deneme3")

# Klasör silme
# os.rmdir("Deneme2")
# os.removedirs("Deneme2/Deneme3")

# Dosya yeniden adlandırma
# os.rename("Deneme.txt", "Deneme2.txt")

# Dosyanın son değiştirilme zamanını al
# print("Dosya Son Değiştirme Zamanı:", datetime.fromtimestamp(os.stat("Deneme2.txt").st_mtime))

# Belirli bir dizindeki dosyaları ve klasörleri yürü
print("Klasör içeriği taranıyor:")
for klasor_yolu, klasor_isimleri, dosya_isimleri in os.walk("c:/Users/ygt/OneDrive/Masaüstü"):
    print("Klasör Yolu:", klasor_yolu)
    print("Klasörler:", klasor_isimleri)
    print("Dosyalar:", dosya_isimleri)
    
    # Belirli bir uzantıya sahip dosyaları filtrele
    for i in dosya_isimleri:
        if i.endswith(".txt"):
            print("Metin Dosyası:", i)

# Belirli bir yolun dosya mı klasör mü olduğunu kontrol etme
yol = "c:/Users/ygt/OneDrive/Masaüstü"
if os.path.isfile(yol):
    print(f"{yol} bir dosyadır.")
elif os.path.isdir(yol):
    print(f"{yol} bir klasördür.")

# Ortam değişkenlerini listeleme
print("Ortam Değişkenleri:")
for anahtar, deger in os.environ.items():
    print(f"{anahtar}: {deger}")

# Sistem bilgisini alma
print("Sistem Bilgisi:")
print("OS Name:", os.name)
if hasattr(os, 'uname'):
    print("Uname Bilgisi:", os.uname())

