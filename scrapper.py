import abc
import requests

class WebSite:
    '''
            1 - __init__:
                1 - initialize the WebSite class instance with metadata of the website to be scrapped.
                arguments:
                    name : the name of the website.
                    url : the website domain - home page url.
                    description : a breif description of the website.

            2 - get_metadata:
                1 - print out the metadata gived in the initialization of the class or by the
                        reset_metadata() method.
                arguments :
                    return_dict : a boolean to get the metadata (name,url,description) as a dictionary ,
                                default value is False.
                    print_data : a boolean to print the metadata , default value is True.

            3 - reset_metadata:
                1 - reset the metadata given in the initialization phase , or set new ones.
                arguments :
                    name : the name of the website.
                    url : the website domain - home page url.
                    description : a breif description of the website.

            4 - start:
                1 - scrap the home page of the website using its home page url given in
                initialization phase or by the reset_metadata() method.
                2 - returns a requests object in case of success or None in other cases.
                arguments : None

    '''
    def __init__(self,name = None,url = None,description = None):
        self.name = name
        self.url = url
        self.description = description

    def get_metadata(self,print_data = True,return_dict = False):
        print('name : ',self.name)
        print('url : ',self.url)
        print('description : ',self.description)
        return True
        if return_dict:
            return { 'name': self.name , 'url': self.url , 'description' : self.description }

    def reset_metadata(self,name = '',url = '',description = ''):
        if isinstance(name,str) and isinstance(url,str) and isinstance(description,str):
            self.name = name
            self.url = url
            self.description = description
        else:
            print('Error : in reset_metadata(name,url,description) - the arguments must be in str type.')
    def start(self):
        if not self.url == None:
            try:
                response = requests.get(self.url)
                print("response returned with {} http code.",response.status_code)
                return response
            except Exception as err:
                print("Error :: in start() : {}".format(str(err)))
                return None
        else:
            print("Error :: in start() : the url property is not setted properly.")
            return None


class Page:
        '''
            1 - __init__ :
                initialize the Page class instance with the base url of the page of the items to be scrapped.
                arguments:
                    baseUrl : the base url of items page to be scrapped.
            2 - set_website :
                set the website object of this page object.
                arguments:
                    website : WebSite object to be setted as parent website of this items page.
                    returnWebSiteObj : boolean to make the set_website() returns the object of the WebSite class which we have setted.

            3 - get_website :
                1 - get the website data of this page object.
                argument:
                    1 - print_data : boolean to print the metadata of the page's object website.
                    2 - returnWebSiteObj : boolean to return a website object of this page object.
            4 - start_consecutive :
                1 - scrap the from begin page to end page consecutively.
                arguments:
                    1 - fromPage : the begining page to start scrap from.
                    2 - endPage : the end page to stop scrap in.
            5 - start_non_consecutive :
                1 - scrap random pages non consecutively.
                arguments:
                    1 - pagesList : int list with pages numbers to be scrapped.
            6 - start_to_end :
                1 - scrap all the pages from a given page to the end of pagination.
                arguments:
                    fromPage : the begining page to start scrap from.
            note:
                the last 3 methods accept an important extra argument wich is a PaginationRule class instance ,
                the object has three methods to get the correct url of each page to be scrapped.
                1 - start_consecutive : uses the PaginationRule object consecutive_pages()  method .
                2 - start_non_consecutive : uses the PaginationRule object non_consecutive_pages() method .
                3 - start_to_end : uses the PaginationRule object to_the_end_pages() method.

        '''
        def __init__(self,baseUrl):
            self.baseUrl = baseUrl
            if not self.baseUrl[-1] == '/':
                self.baseUrl = self.baseUrl + '/'
            self.website = None
            self.urls = None

            print("the base url setted properly : {}".format(self.baseUrl))
        def set_website(self,website,returnWebSiteObj = False):
            self.website = website
            if not isinstance(self.website,WebSite):
                print("Error :: in set_website(website) : the website argument must an instance of the WebSite class.")
                return None
            else:
                print("Website object is setted properly for this page object.")
                if returnWebSiteObj:
                    return returnWebSiteObj
        def get_website(self,print_data = True,returnWebSiteObj = True):
            if isinstance(self.website,WebSite):
                if print_data:
                    print('name : ',self.website.name)
                    print('url : ',self.website.url)
                    print('description : ',self.website.description)
                    return True
                if returnWebSiteObj:
                    return self.website
            else:
                print("Error :: in get_website() : this page object has no website object setted.")
                return None



        def start_consecutive(self,fromPage,toPage,paginationRule):
            if not isinstance(fromPage,int) and isinstance(endPage,int) and isinstance(paginationRule,PaginationRule):
                print("Error :: in start_consecutive : arguments must be with int type , PaginationRule argument must be a PaginationRule object.")
                return None
            else:
                if toPage < fromPage:
                    print("Error :: in start_consecutive : second argument must be bigger than first argument.")
                    return None
            self.fromPage = fromPage
            self.toPage = toPage
            self.urls = paginationRule.consecutive_pages(self.baseUrl,self.fromPage,self.toPage)

        def start_non_consecutive(self,pagesList,paginationRule):
            if not isinstance(pagesList,list) and len(pagesList) >= 1 and isinstance(paginationRule,PaginationRule):
                print("Error :: in start_non_consecutive : argument must be a list with more than one item , PaginationRule argument must be a PaginationRule object.")
            self.pagesList = pagesList
            self.urls = paginationRule.non_consecutive_pages(self.baseUrl,self.pagesList)

        def start_to_end(self,fromPage,paginationRule):
            if not isinstance(fromPage,int) and isinstance(paginationRule,PaginationRule):
                print("Error :: start_to_end : argument must be with int type , PaginationRule argument must be a PaginationRule object.")
                return None
            self.fromPage = fromPage
            self.urls = paginationRule.to_the_end_pages(self.baseUrl,self.fromPage)


        def begin_the_play(self,item):
            if not self.urls == None and isinstance(item,Items):
                try:
                    for url in self.urls:
                        response = requests.get(url)

                except Exception as err:
                    print("Error :: in begin_the_play : {}.".format(str(err)))
                    print("operation stopped.")
                    return None
            else:
                print("Error :: in begin_the_play : the urls attribute is not setted properly , item argument must be an instance of Items class.")
                return None




class PaginationRule(abc.ABC):
    @abc.abstractmethod
    def consecutive_pages(self,url,fromPage,toPage,rule = ''):  # rule argument for cases where pagination in this form   url/?page=Page_number , where rule = ?page=
        pass
    @abc.abstractmethod
    def non_consecutive_pages(self,url,pagesList,rule = ''):
        pass
    @abc.abstractmethod
    def to_the_end_pages(self,url,fromPage,rule = ''):
        pass



class OuedKniss(PaginationRule):
    def consecutive_pages(self,url,fromPage,toPage):
        for page in range(fromPage,toPage + 1):
            yield (url + str(page))
    def non_consecutive_pages(self,url,pagesList):
        for page in pagesList:
            yield (url + str(page))
    def to_the_end_pages(self,url,fromPage):
        stopCondition = 'not setted yet'
        while not stopCondition:
            yield (url + str(page))

class Items:
    def __init__(self,title='',image='',price='',description='',date=''):
        self.titleSelector = title
        self.imageSelector = image
        self.priceSelector = price
        self.descriptionSelector = description
        self.dateSelector = date



'''
website = WebSite('OuedKniss','http://www.ouedKniss.dz','e-commerce web site')
page = Page("https://www.ouedkniss.com/telephones")
ouedKniss = OuedKniss()
page.start_consecutive(1,3,ouedKniss)
item = Items()
page.begin_the_play(item)'''
