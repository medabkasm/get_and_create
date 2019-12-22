
class WebSite:
    '''
            1 - initialize the class instant with metadata of the website to be scrapped.
                name : the name of the website.
                url : the website domain - home page url.
                description : a breif description of the website.
            2 - get_metadata:
                    print out the metadata gived in the initialization of the class or by the
                    reset_metadata() method.
            3 - reset_metadata:
                    reset the metadata given in the initialization phase , or set new ones.
            4 - start:
                    scrap the home page of the website using its home page url given in
                    initialization phase or by the reset_metadata() method.
                    returns a requests object in case of success or None in other cases.
    '''
    def __init__(self,name = None,url = None,description = None):
        self.name = name
        self.url = url
        self.description = description
    def get_metadata(self):
        print('name : ',self.name)
        print('url : ',self.url)
        print('description : ',self.description)
    def reset_metadata(self,name = '',url = '',description = ''):
        if isinstance(name,str) and isinstance(url,str) and isinstance(description,str):
            self.name = name
            self.url = url
            self.description = description
        else:
            print('the arguments must be in str type.')
    def start(self):
        if not self.url == None:
            try:
                import requests
                response = requests.get(self.url)
                return response
            except Exception as err:
                print("Error :: error in start() : {}".format(str(err)))
                return None
        else:
            print("Error :: the url is not setted properly.")
            return Null
