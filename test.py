import requests
from bs4 import BeautifulSoup as soup

headers = {
        "user-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
        }
response = requests.get("https://hanoutdz.com/categorie-produit/accessoires-auto/page/1/",headers = headers)
items = soup(response.text,'html.parser').select(".item-detail")
#error= soup(response.text,'html.parser').select(".content_404")

for item in items:
    print("title : ",item.select(".item-content h4")[0].text)
    print("link : ",item.select("a")[0].get("href"))
    print("image : ",item.select("img")[0].get("data-lazy-src"))
    print("price : ",item.select(".woocommerce-Price-amount")[0].text)

    
