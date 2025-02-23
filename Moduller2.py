import requests
from bs4 import BeautifulSoup
import sys

# UTF-8 çıkışı için ayar
sys.stdout.reconfigure(encoding="utf-8")

# URL'yi belirt
url = "https://www.omu.edu.tr/tr"

# URL'ye istek gönderme
response = requests.get(url)

# HTTP isteği başarılı mı diye kontrol et
if response.status_code == 200:
    print("Başarılı istek!")
else:
    print(f"İstek başarısız! HTTP Durum Kodu: {response.status_code}")
    sys.exit()

# Yanıtın encoding türünü ayarlama
response.encoding = response.apparent_encoding

# HTML içeriğini al
html_icerigi = response.content

# BeautifulSoup ile HTML'yi parse etme
soup = BeautifulSoup(html_icerigi, "html.parser")

# Sayfadaki tüm <a> etiketlerini bulma ve href özniteliklerini almak
hrefs = [a.get("href") for a in soup.find_all("a") if a.get("href")]

# 'None', '#' veya 'javascript:void(0)' içeren linkleri filtreleme
filtered_hrefs = [link for link in hrefs if link and link not in ["#", "javascript:void(0)"]]
print(f"Filtrelenmiş Bağlantılar: {filtered_hrefs}")

# <h2 class="title"> etiketini bulma ve içindeki <a> etiketinden metni ve linki almak
h2_tag = soup.find("h2", class_="title")
if h2_tag:
    a_tag = h2_tag.find("a")
    if a_tag:
        link = a_tag.get("href")  # Bağlantıyı al
        text = a_tag.text.strip()  # Metni al
        print(f"Link: {link}")
        print(f"Metin: {text}")
else:
    print("Sayfada <h2 class='title'> etiketi bulunamadı.")

# Sayfadaki tüm başlıkları almak (örneğin <h1>, <h2>, <h3> etiketleri)
for header in soup.find_all(['h1', 'h2', 'h3']):
    print(f"{header.name}: {header.text.strip()}")

# Sayfadaki tüm resimleri almak (örneğin <img> etiketlerindeki src)
for img in soup.find_all('img'):
    img_src = img.get('src')
    if img_src:
        print(f"Resim Linki: {img_src}")

# Sayfada bulunan tüm linklerin sayısını yazdırma
link_count = len(filtered_hrefs)
print(f"Sayfada toplam {link_count} geçerli bağlantı var.")

# Sayfada bulunan tüm paragraf metinlerini almak (<p> etiketleri)
for paragraph in soup.find_all('p'):
    print(f"Paragraf: {paragraph.text.strip()}")

# Sayfadaki tüm form etiketlerini almak (<form> etiketleri)
for form in soup.find_all('form'):
    print(f"Form: {form}")

# Kullanışlı bir hata kontrolü eklemek (sayfa boş ya da beklenmeyen şekilde gelirse)
if not soup:
    print("Sayfa içeriği parse edilemedi.")
    sys.exit()

# Sayfa başlığını yazdırma (başlık <title> etiketi)
title = soup.title
print(f"Sayfa Başlığı: {title.text.strip()}")

# Page scraping'in sonuna geldik.
print("Web sayfası başarıyla işlendi.")
