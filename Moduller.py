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
