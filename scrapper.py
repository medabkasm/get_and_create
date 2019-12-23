
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
                import requests
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

        '''
        def __init__(self,baseUrl):
            self.baseUrl = baseUrl
            self.website = None
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
