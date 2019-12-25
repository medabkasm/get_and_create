import requests
from bs4 import BeautifulSoup as soup

CRED    = "\33[31m"
CGREEN  = "\33[32m"
CEND = "\033[0m"


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
            print(CRED+"Error : in reset_metadata : the arguments must be with str type."+CEND)
    def start(self):
        if not self.url == None:
            try:
                response = requests.get(self.url)
                print(CGREEN+"response returned with {} http code.".format(response.status_code)+CEND)
                return response
            except Exception as err:
                print(CRED+"Error :: in start : {}".format(str(err))+END)
                return None
        else:
            print(CRED+"Error :: in start : the url property is not setted properly."+CEND)
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
            self.paginationRule = None

            print(CGREEN+"the base url is setted properly : {}".format(self.baseUrl)+CEND)
        def set_website(self,website,returnWebSiteObj = False):
            self.website = website
            if not isinstance(self.website,WebSite):
                print(CRED+"Error :: in set_website : the website argument must an instance of the WebSite class."+CEND)
                return None
            else:
                print(CGREEN+"Website object is setted properly for this page object."+CEND)
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
                print(CRED+"Error :: in get_website : this page object has no website object setted."+CEND)
                return None



        def start_consecutive(self,fromPage,toPage,paginationRule):
            if not isinstance(fromPage,int) and isinstance(endPage,int) and isinstance(paginationRule,PaginationRule):
                print(CRED+"Error :: in start_consecutive : arguments must be with int type , PaginationRule argument must be a PaginationRule object."+CEND)
                return None
            else:
                if toPage < fromPage:
                    print(CRED+"Error :: in start_consecutive : second argument must be bigger than first argument."+CEND)
                    return None
            self.fromPage = fromPage
            self.toPage = toPage
            self.urls = paginationRule.consecutive_pages(self.baseUrl,self.fromPage,self.toPage)
            self.paginationRule = paginationRule
            return True

        def start_non_consecutive(self,pagesList,paginationRule):
            if not isinstance(pagesList,list) and len(pagesList) >= 1 and isinstance(paginationRule,PaginationRule):
                print(CRED+"Error :: in start_non_consecutive : argument must be a list with more than one item , PaginationRule argument must be a PaginationRule object."+CEND)
            self.pagesList = pagesList
            self.urls = paginationRule.non_consecutive_pages(self.baseUrl,self.pagesList)
            print(self.urls)
            self.paginationRule = paginationRule
            return True

        def start_to_end(self,fromPage,paginationRule):
            if not isinstance(fromPage,int) and isinstance(paginationRule,PaginationRule):
                print(CRED+"Error :: start_to_end : argument must be with int type , PaginationRule argument must be a PaginationRule object."+CEND)
                return None
            self.fromPage = fromPage
            self.urls = paginationRule.to_the_end_pages(self.baseUrl,self.fromPage)
            self.paginationRule = paginationRule
            return True

        def begin_the_play(self,item,urlsList = [],text = True,csv = False,json = False):
            if not self.urls == None and isinstance(item,Items):
                if  isinstance(item.containerSelector,str) and len(item.containerSelector) > 1 :
                    for url in self.urls:
                        try:
                            response = requests.get(url)
                        except:
                            print(CRED+"Error :: in begin_the_play : with {}.".format(url)+CEND)
                            continue
                        html = soup(response.text,'html.parser')
                        data = self.__start(item,html,item.containerSelector)
                        print(data)
                        print(len(data))


                else:
                    print(CRED+"Error :: in begin_the_play : the container selector // {} // is not setted properly.".format(item.containerSelector)+CEND)
                    return None
            else:
                print(CRED+"Error :: in begin_the_play : the urls attribute is not setted properly , item argument must be an instance of Items class."+CEND)
                return None

        def __get_containers(self,item,html,containerSelector):
            try:
                containers = html.select(containerSelector)
                return containers
            except Exception as err:
                print(CRED+"Error :: in begin_the_play : {}.".format(str(err))+CEND)
                print(CRED+"container with selector //  {}  // cannot be fetched properly.".format(containerSelector)+CEND)
                return None

        def __get_data(self,container,dataSelector):
            try:
                data = container.select(dataSelector)[0]
                return data
            except Exception as err:
                print(CRED+"Error :: in begin_the_play : data with // {} // selector cannot be fetched properly.".format(dataSelector)+CEND)
                return None

        def __save(self,item,containers):

            dataList = []
            dataDict = {}
            for container in containers:

                if item.titleSelector:
                    title = self.__get_data(container,item.titleSelector)
                    if title:
                        title = self.paginationRule.filter(title).title_filter()
                if item.imageSelector:
                    image = self.__get_data(container,item.imageSelector)
                    if image:
                        image = self.paginationRule.filter(image).img_filter()
                if item.priceSelector:
                    price = self.__get_data(container,item.priceSelector)
                    if price:
                        price = self.paginationRule.filter(price).price_filter()
                if item.descriptionSelector:
                    description = self.__get_data(container,item.descriptionSelector)
                    if description:
                        description = self.paginationRule.filter(description).description_filter()
                if item.dateSelector:
                    date = self.__get_data(container,item.dateSelector)
                    data = None
                    if date:
                        date = self.paginationRule.filter(date).date_filter()
                if item.detailsLink:
                    detailsLink = self.__get_data(container,item.detailsLink)
                    if detailsLink:
                        detailsLink = self.paginationRule.filter(detailsLink).detailsLink_filter()

                dataDict = {
                    "title" : title ,
                    "link"  : detailsLink,
                    "image" : image,
                    "price" : price,
                    "description" : description,
                    "date" : None ,
                    }
                dataList.append(dataDict.copy())

            return dataList


        def __start(self,item,html,containerSelector):
            containers = self.__get_containers(item,html,containerSelector)
            if containers:
                return self.__save(item,containers)
            else:
                return None




class Items:
    def __init__(self,container = '' ,title = '',link = '',image = '',price = '',description = '',date = ''):
        self.containerSelector = container
        self.titleSelector = title
        self.imageSelector = image
        self.priceSelector = price
        self.descriptionSelector = description
        self.dateSelector = date
        self.detailsLink = link
