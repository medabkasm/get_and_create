import abc

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

    class filter:
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

    class filter:
        def __init__(self,data = ''):
            self.data = data
        def img_filter(self):
            if self.data:
                try:
                    data = self.data.split("(")[-1].split(")")[0]
                    self.data = None
                    return data
                except:
                    return None
            return None

        def detailsLink_filter(self):
            if self.data:
                try:
                    data = "https://www.ouedkniss.com/" + self.data.get("href")
                    self.data = None
                    return data
                except:
                    return None
            return None

        def price_filter(self):
            return self.__global_filter()
        def description_filter(self):
            return self.__global_filter()
        def date_filter(self):
            return self.__global_filter()
        def title_filter(self):
            return self.__global_filter()

        def __global_filter(self):
            if self.data:
                try:
                    data = self.data.text
                    self.data = None
                    return data
                except:
                    return None
            return None
