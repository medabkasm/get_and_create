from scrapper import *
from extenders import *
import resource
from testing import Test
from saver import Save
import json

if __name__ == "__main__":

    # ouedKniss test
    website = WebSite('OuedKniss','https://www.ouedKniss.com','e-commerce web site')
    page = Page("https://www.ouedkniss.com/telephones")
    ouedKniss = OuedKniss()
    item = Items()
    with open('selectors.json') as file:
        selectors = file.read()
        selectorsJson = json.loads(selectors)
        ouedknissSelectors = selectorsJson.get('ouedkniss')
        jumiaSelectors = selectorsJson.get('jumia')
        hanoutDzSelectors = selectorsJson.get('hanoutDz')

    item.containerSelector = ouedknissSelectors['containerSelector']
    item.titleSelector = ouedknissSelectors['titleSelector']
    item.detailsLink = ouedknissSelectors['detailsLink']
    item.descriptionSelector = ouedknissSelectors['descriptionSelector']
    item.priceSelector = ouedknissSelectors['priceSelector']
    item.imageSelector = ouedknissSelectors['imageSelector']

    urls = ["https://www.ouedkniss.com/cosmetiques/1","https://www.ouedkniss.com/telephones/1"]
    test = Test(website,page,ouedKniss,item)
    data = test.start_consecutive(1,3)
    #data = test.start_non_consecutive([1,3,4])
    #data = test.start_to_end(10)
    #data = test.start_with_urls(urls,ouedKniss)
    save = Save(data)
    save.to_json()
    save.to_csv()


    '''
    # jumia test
    website = WebSite('jumia','https://www.jumia.dz/','e-commerce web site')
    page = Page("https://www.jumia.dz/telephones-smartphones/")
    jumia = Jumia()
    item = Items()

    item.containerSelector = jumiaSelectors['containerSelector']
    item.titleSelector = jumiaSelectors['titleSelector']
    item.detailsLink = jumiaSelectors['detailsLink']
    item.priceSelector = jumiaSelectors['priceSelector']
    item.imageSelector = jumiaSelectors['imageSelector']

    urls = ["https://www.jumia.dz/telephones-smartphones/","https://www.jumia.dz/maison-bureau-meubles/"]
    test = Test(website,page,jumia,item)
    data = test.start_consecutive(1,3)
    #data = test.start_non_consecutive([1,3,4])
    #data = test.start_to_end(10)
    #data = test.start_with_urls(urls,jumia)
    print(data)

    # hanoutDz test
    website = WebSite('hanoutDz','https://hanoutdz.com/','e-commerce web site')
    page = Page("https://hanoutdz.com/categorie-produit/accessoires-auto/")
    hanoutDz = HanoutDz()
    item = Items()

    item.containerSelector = hanoutDzSelectors['containerSelector']
    item.titleSelector = hanoutDzSelectors['titleSelector']
    item.detailsLink = hanoutDzSelectors['detailsLink']
    item.priceSelector = hanoutDzSelectors['priceSelector']
    item.imageSelector = hanoutDzSelectors['imageSelector']

    urls = ["https://hanoutdz.com/categorie-produit/accessoires-auto/","https://hanoutdz.com/categorie-produit/sante-beaute/coiffure-soincheveux/"]
    test = Test(website,page,hanoutDz,item)
    data = test.start_consecutive(1,3)
    #data = test.start_non_consecutive([1,3,4])
    #data = test.start_to_end(10)
    #data = test.start_with_urls(urls,hanoutDz)
    print(data)

    '''
