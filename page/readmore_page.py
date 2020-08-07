import time

from page.base_page import BasePage

#阅读列表页面
class ReadMorePage(BasePage):
    def read_one(self,read_name):
        self._params['read_name'] = read_name
        return self.step('../steps/readmore_page.yaml', 'read_one')

