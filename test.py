import requests
from bs4 import BeautifulSoup as soup


response = requests.get("https://www.jumia.dz/telephones-smartphones/")
print("done")
object = soup(response.text,'html.parser').select(".sku")
for item in object:
    if item.a:
        print("brand = ",item.select(".title .brand")[0].text)
        print("name = ",item.select(".title .name")[0].text)
        print("link = ",item.select("a")[0].get("href"))
        print("price = ",item.select(".price-box")[0].text)
    if item.img:
        print("image = ",item.select(".image-wrapper")[0].img.get("src"))
