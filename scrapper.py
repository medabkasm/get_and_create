
class WebSite:
    '''
            1 - __init__: -------------------------------------------------------------------------
                1 - initialize the class instant with metadata of the website to be scrapped.
                arguments:
                    name : the name of the website.
                    url : the website domain - home page url.
                    description : a breif description of the website.

            2 - get_metadata: ---------------------------------------------------------------------
                1 - print out the metadata gived in the initialization of the class or by the
                        reset_metadata() method.
                arguments :
                    return_dict : a boolean to get the metadata (name,url,description) as a dictionary ,
                                default value is False.
                    print_data : a boolean to print the metadata , default value is True.

            3 - reset_metadata: -------------------------------------------------------------------
                1 - reset the metadata given in the initialization phase , or set new ones.
                arguments :
                    name : the name of the website.
                    url : the website domain - home page url.
                    description : a breif description of the website.

            4 - start: ----------------------------------------------------------------------------
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
        if return_dict:
            return { 'name': self.name , 'url': self.url , 'description' : self.description }

    def reset_metadata(self,name = '',url = '',description = ''):
        if isinstance(name,str) and isinstance(url,str) and isinstance(description,str):
            self.name = name
            self.url = url
            self.description = description
        else:
            print('Error : reset_metadata(name,url,description) - the arguments must be in str type.')
    def start(self):
        if not self.url == None:
            try:
                import requests
                response = requests.get(self.url)
                print("response returned with {} http code.",response.status_code)
                return response
            except Exception as err:
                print("Error :: error in start() : {}".format(str(err)))
                return None
        else:
            print("Error :: error in start() : the url property is not setted properly.")
            return None
