from scrapper import WebSite , Page , Items
from extenders import OuedKniss


print("heeloo")
if __name__ == "__main__":

    website = WebSite('OuedKniss','https://www.ouedKniss.com','e-commerce web site')
    page = Page("https://www.ouedkniss.com/telephones")
    ouedKniss = OuedKniss()
    page.start_consecutive(1,2,ouedKniss)
    page.set_website(website)
    page.get_website()
    item = Items()

    item.containerSelector = ".annonce_left"
    item.titleSelector = ".annonce_titre h2"
    item.detailsLink = ".annonce_titre a"
    item.descriptionSelector = ".annonce_description_preview"
    item.priceSelector = ".annonce_prix"
    item.imageSelector = ".annonce_image_img"


    page.begin_the_play(item)
