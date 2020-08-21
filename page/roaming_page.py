from page.base_page import BasePage

#流量上网页面
class RoamingPage(BasePage):
    def exchange_one(self):
        return self.step('../steps/roaming_page.yaml', 'exchange_one')

    def buy_one(self):
        return self.step('../steps/roaming_page.yaml', 'buy_one')

    def help(self):
        return self.step('../steps/roaming_page.yaml', 'help')