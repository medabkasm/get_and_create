import requests
from bs4 import BeautifulSoup as soup
from extenders import PaginationRule
CRED    = "\33[31m"
CGREEN  = "\33[32m"
CEND = "\033[0m"

'''
    created by medabkasm O-O -> github account : https://github.com/medabkasm
'''

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

        if print_data:
            print('name : ',self.name)
            print('url : ',self.url)
            print('description : ',self.description)

        if return_dict:
            return { 'name': self.name , 'url': self.url , 'description' : self.description }

        return True

    def reset_metadata(self,name = '',url = '',description = ''):
        if isinstance(name,str) and isinstance(url,str) and isinstance(description,str):
            self.name = name
            self.url = url
            self.description = description
        else:
            print(CRED+"Error : in reset_metadata : the arguments must be with str type."+CEND)
    def start(self,headers = {}):
        if headers and isinstance(headers,dict):
            self.headers = headers
        else:
            self.headers = {
                    "user-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
                    }
        if not self.url == None:
            try:
                response = requests.get(self.url,headers = self.headers)
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
                1 - initialize the Page class instance with the base url of the page of the items to be scrapped.
                arguments:
                    baseUrl : the base url of items page to be scrapped.
            2 - set_website :
                1 - set the website object of this page object.
                arguments:
                    website : WebSite object to be setted as parent website of this items page.
                    returnWebSiteObj : boolean to make the set_website() returns the object of the WebSite class which we have setted.

            3 - get_website :
                1 - get the website data of this page object.
                argument:
                    print_data : boolean to print the metadata of the page's object website.
                    returnWebObj : boolean to return a website object of this page object.
            4 - start_consecutive :
                1 - scrap the from begin page to end page consecutively.
                arguments:
                    fromPage : the begining page to start scrap from.
                    endPage : the end page to stop scrap in.
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
            7 - begin_the_play :
                1 - start scrapping operation and returns a generator object of the fetched data with the help of other private methods(mentioned down).
                arguments:
                    item : an object of Item class to get css selectors used to fetched the data.
                    urlsList : a list of hard coded urls used to prevent using any methods (start_consecutive , start_non_consecutive , start_to_end).
                    note:
                        a call with urlsList , will override the functionality of (start_consecutive , start_non_consecutive , start_to_end)
                            if they get called befor it to set urls , you need to set the attribute paginationRule to a PaginationRule class instance in this case .
            8 - __get_containers :
                1 - to get the page elements containers , where each container contains all the data needed to be fetched , returns list of all containers objects (soup object).
                arguments:
                    item : an object of Item class to get css selectors used to fetched the data.
                    html : page html object (soup object) ,used to parse containers from it.
                    containerSelector : container css selector to be fetched.
            9 - __get_data :
                1 - to fetched data from the container object , and returns the parsed data.
                arguments:
                    container : container object used to fetch the data form it.
                    dataSelector : css selector used to parse the data from the container object.
            10 - __save :
                1 - returns the clean form of the data fetched as a list of dictionaries with
                    the help of the __get_data method and some filters found in the item object.
                arguments:
                    item : an object of Item class to get filters used to filter the data.
                    containers : containers list returned by __get_containers method.
            11 - __start :
                1 - helper method to start the real scapping operation using __save and __get_containers methods ,
                    it returns the data returned by __save method.



        '''
        def __init__(self,baseUrl,headers = {}):
            self.baseUrl = baseUrl
            if not self.baseUrl[-1] == '/':
                self.baseUrl = self.baseUrl + '/'
            self.website = None
            self.urls = None
            self.paginationRule = None
            if headers and isinstance(headers,dict):
                self.headers = headers
            else:
                self.headers = {
                        "user-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
                        }

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

        def begin_the_play(self,item,urlsList = []):

            if urlsList and isinstance(urlsList,list):
                self.urls = urlsList
            if not self.urls == None and isinstance(item,Items):
                if  isinstance(item.containerSelector,str) and len(item.containerSelector) > 1 :
                    for url in self.urls:
                        try:
                            response = requests.get(url ,headers = self.headers)
                        except:
                            print(CRED+"Error :: in begin_the_play : with {}.".format(url)+CEND)
                            continue
                        html = soup(response.text,'html.parser')
                        data = self.__start(item,html,item.containerSelector)
                        if data:
                            yield (data)
                        else:
                            break

                else:
                    print(CRED+"Error :: in begin_the_play : the container selector // {} // is not setted properly.".format(item.containerSelector)+CEND)
                    return None
            else:
                print(CRED+"Error :: in begin_the_play : the urls attribute is not setted properly , item argument must be an instance of Items class."+CEND)
                return None

            print(CGREEN + "end of pages !"+CEND)
            return

        def __get_containers(self,item,html,containerSelector):
            try:
                containers = html.select(containerSelector)
                if containers:
                    return containers
                return None
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
                title = None
                image = None
                price =None
                description = None
                date = None
                detailsLink = None
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
                    "date" : date ,
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
    '''
        initialize an object with css selector of each item ,to be used by the begin_the_play method of the Page class.
    '''
    def __init__(self,container = '' ,title = '',link = '',image = '',price = '',description = '',date = ''):
        self.containerSelector = container
        self.titleSelector = title
        self.imageSelector = image
        self.priceSelector = price
        self.descriptionSelector = description
        self.dateSelector = date
        self.detailsLink = link
