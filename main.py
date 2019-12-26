from scrapper import *
from extenders import *
import resource


if __name__ == "__main__":

    def ouedKniss_test():
        website = WebSite('OuedKniss','https://www.ouedKniss.com','e-commerce web site')
        page = Page("https://www.ouedkniss.com/telephones")
        ouedKniss = OuedKniss()
        #page.start_to_end(2260,ouedKniss)
        #page.start_consecutive(1,2,ouedKniss)
        #page.start_non_consecutive([1,3,10,11],ouedKniss)
        page.set_website(website)
        page.get_website()
        item = Items()

        item.containerSelector = ".annonce_left"
        item.titleSelector = ".annonce_titre h2"
        item.detailsLink = ".annonce_titre a"
        item.descriptionSelector = ".annonce_description_preview"
        item.priceSelector = ".annonce_prix"
        item.imageSelector = ".annonce_image_img"
        urls = ["https://www.ouedkniss.com/cosmetiques/1","https://www.ouedkniss.com/telephones/1"]
        page.paginationRule = ouedKniss
        data = page.begin_the_play(item,urls)
        #data = page.begin_the_play(item)
        for el in data:
            print(el)

    def jumia_test():
        website = WebSite('jumia','https://www.jumia.dz/','e-commerce web site')
        page = Page("https://www.jumia.dz/telephones-smartphones/")
        jumia = Jumia()
        #page.start_to_end(4,jumia)
        page.start_consecutive(1,6,jumia)
        #page.start_non_consecutive([1,3,10,11],jumia)
        page.set_website(website)
        page.get_website()
        item = Items()

        item.containerSelector = ".sku"
        item.titleSelector = ".title .name"
        item.detailsLink = "a"
        item.priceSelector = ".price-box"
        item.imageSelector = ".image-wrapper"
        urls = ["https://www.jumia.dz/telephones-smartphones/","https://www.jumia.dz/maison-bureau-meubles/"]
        page.paginationRule = jumia
        #data = page.begin_the_play(item)
        data = page.begin_the_play(item,urls)
        print(data)
        for el in data:
            print(el)

    jumia_test()
