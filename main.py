from scrapper import *
from extenders import *
import resource
from testing import Test
from saver import Save

if __name__ == "__main__":

    # ouedKniss test
    website = WebSite('OuedKniss','https://www.ouedKniss.com','e-commerce web site')
    page = Page("https://www.ouedkniss.com/telephones")
    ouedKniss = OuedKniss()
    item = Items()
    item.containerSelector = ".annonce_left"
    item.titleSelector = ".annonce_titre h2"
    item.detailsLink = ".annonce_titre a"
    item.descriptionSelector = ".annonce_description_preview"
    item.priceSelector = ".annonce_prix"
    item.imageSelector = ".annonce_image_img"
    urls = ["https://www.ouedkniss.com/cosmetiques/1","https://www.ouedkniss.com/telephones/1"]
    test = Test(website,page,ouedKniss,item)
    data = test.start_consecutive(1,3)
    #data = test.start_non_consecutive([1,3,4])
    #data = test.start_to_end(10)
    #data = test.start_with_urls(urls,ouedKniss)
    save = Save(data)
    save.to_json()
    save.to_csv()


    '''# jumia test
    website = WebSite('jumia','https://www.jumia.dz/','e-commerce web site')
    page = Page("https://www.jumia.dz/telephones-smartphones/")
    jumia = Jumia()
    item = Items()
    item.containerSelector = ".sku"
    item.titleSelector = ".title .name"
    item.detailsLink = "a"
    item.priceSelector = ".price-box"
    item.imageSelector = ".image-wrapper"
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
    item.containerSelector = ".item-detail"
    item.titleSelector = ".item-content h4"
    item.detailsLink = "a"
    item.imageSelector = "img"
    item.priceSelector = ".woocommerce-Price-amount"
    urls = ["https://hanoutdz.com/categorie-produit/accessoires-auto/","https://hanoutdz.com/categorie-produit/sante-beaute/coiffure-soincheveux/"]
    test = Test(website,page,hanoutDz,item)
    data = test.start_consecutive(1,3)
    #data = test.start_non_consecutive([1,3,4])
    #data = test.start_to_end(10)
    #data = test.start_with_urls(urls,hanoutDz)
    print(data)'''
