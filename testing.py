class Test:
    def __init__(self,website,page,paginationRule,item):
        self.page = page
        self.paginationRule = paginationRule
        self.item = item
        self.page.set_website(website)
        self.page.get_website()
    def start_consecutive(self,fromPage,toPage):
        self.page.start_consecutive(fromPage,toPage,self.paginationRule)
        data = self.page.begin_the_play(self.item)
        return data
    def start_non_consecutive(self,urlsList):
        self.page.start_non_consecutive(urls,self.paginationRule)
        data = self.page.begin_the_play(self.item)
        return data
    def start_to_end(self,fromPage):
        self.page.start_to_end(fromPageEnd,self.paginationRule)
        data = self.page.begin_the_play(self.item)
        return data
    def start_with_urls(self,urls,paginationRule):
        self.page.paginationRule = paginationRule
        data = self.page.begin_the_play(self.item,urls)
        return data
