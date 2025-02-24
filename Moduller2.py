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




******************************************************************************OMU************************************************************************************


import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://oidb.omu.edu.tr/tr"
response = requests.get(url)

if response.status_code == 200:
    print("Successful")
else:
    print(f"Request failed: Hata kodu = {response.status_code}")
    sys.exit()

response.encoding = response.apparent_encoding

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

# 'news' class'ı ile başlayan section etiketini buluyoruz
section = soup.find("section", class_="news")

# İçindeki her bir haber öğesini bulalım
if section:
    news_items = section.find_all("div", class_="news-item")
    for news in news_items:
        # İçeriği yazdıralım
        title = news.find("h2", class_="title")
        if title:
            link = title.find("a")
            if link:
                print(f"Metin: {link.get_text(strip=True)}")
a = input("q: ya bas cik")
if a == "q":
    sys.exit


*************************************************************************ODÜ******************************************************************************************

import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://www.odu.edu.tr/"

response = requests.get(url)
if response.status_code == 200:
    print("Successful!")
else:
    print("Connection failed. Code:{}".format(response.status_code))
    sys.exit()
response.encoding = response.apparent_encoding
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

divs = soup.find("div",{"class":"col-md-6"})

if divs:
    announcements_items = divs.find_all("a",target = "_blank")
    for news in announcements_items:
        if news:
            print(f"Metin: {news.get_text(strip=True)}")

a = input("Cikmak icin: 'q' bas enterla")
if a == "q":
    sys.exit



**********************************************************************AÜ**********************************************************************************


import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding = "utf-8")

url = "https://oidb.ankara.edu.tr/"

response = requests.get(url)
if response.status_code == 200:
    print("Successful!")
else:
    print("Connection failed. Hata kodu {}".format(response.status_code))
    sys.exit()
response.encoding = response.apparent_encoding
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

section_element = soup.find("section", {"class": "fusion-columns columns fusion-columns-1 columns-1"})
if section_element:
    news_articles = soup.find_all("article", {"class": "post fusion-column column col col-lg-12 col-md-12 col-sm-12"})
    for article in news_articles:
        recent_posts = article.find_all("div", {"class": "recent-posts-content"})
        if recent_posts:
            for post in recent_posts:
                post_title = post.find("h4", {"class": "entry-title"})
                if post_title:
                    links = post_title.find_all("a")
                    for link in links:
                        href = link.get("href")
                        text = link.text
                        print(f"{text}\n")


**********************************************************************IMDB**********************************************************************************
import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url,headers=headers)
if response.status_code == 200:
    print("Successful")
else:
    print("Connection failed. Code = {}".format(response.status_code))
    sys.exit()

response.encoding = response.apparent_encoding

html_icerigi = response.content
soup = BeautifulSoup(html_icerigi, "html.parser")

li = soup.find_all("h3",{"class":"ipc-title__text"})
if li:
    for i in li:
        moviename = i.text
        print(moviename)

**********************************************************************Doviz**********************************************************************************

import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding="utf-8")
url = "https://www.doviz.com/"

response = requests.get(url)
if response.status_code == 200:
    print("Successful")
else:
    print("Connection failed Error Code: {}".format(response.status_code))

response.encoding = response.apparent_encoding
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi, "html.parser")

degerler = soup.find_all("span", {"class": "value"})
if degerler:
    for i in degerler:
        # data-socket-key özelliği varsa almak için kontrol
        data_socket_key = i.get("data-socket-key", "N/A")  # Eğer yoksa 'N/A' döner
        print(f"{data_socket_key} : {i.text.strip()}")
else:
    print("Döviz verisi bulunamadı.")

