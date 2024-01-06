import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

# Gerekli Listeler
url_list = []
price_list = []
propTitles = []
propValues = []

# Özelliklerin çekilmesi
for i in range(1, 200):
    url = 'https://www.emlakjet.com/satilik-konut/istanbul-beyoglu/' + str(i) + '/'
    r = requests.get(url)  # Hazırlanan url'e istek yapılması
    source = BeautifulSoup(r.content, "lxml")  # İstek yapılan sayfanın içeriğinin çekilmesi

    urls = source.find_all("div", attrs={"class": "_3qUI9q"})
    for url in urls:
        url_ilan = "https://www.emlakjet.com/" + url.a.get("href")
        url_list.append(url_ilan)
        print(url_ilan)

        r_ilan = requests.get(url_ilan)  # Bulunan linke tekrar istek atılması
        source_ilan = BeautifulSoup(r_ilan.content, "lxml")  # Veri içeriğinin çekilmesi

        properties = source_ilan.find_all("div", attrs={"class": "_35T4WV"})
        prop_dict = {}  # Her bir özelliği geçici bir sözlükte topluyoruz
        for prop in properties:
            div_elements = prop.find_all("div", attrs={"class": "_1bVOdb"})
            prop_title = div_elements[0].text
            prop_value = div_elements[1].text
            prop_dict[prop_title] = prop_value

        propTitles.append(prop_dict)

    prices = source.find_all("p", attrs={"class": "_2C5UCT"})
    for price in prices:
        price_list.append(price.text)
        print(price.text)

print(str(len(url_list)) + "adet link bulundu")
print(str(len(price_list)) + "adet fiyat bulundu")
print(str(len(propTitles)) + "adet özellik başlığı bulundu")
print(str(len(propValues)) + "adet özellik bulundu")

# Url ve fiyatları bir data frame yazma
df_urls = pd.DataFrame()
df_urls["urls"] = url_list
df_urls["prices"] = price_list


homes = len(url_list)

# Başlıkları kullanarak url ve fiyat ile yeni bir data frame oluşturma
df = pd.DataFrame(propTitles)
df["url"] = url_list
df["prices"] = price_list

df.to_excel("emlak.xlsx", index=False)
