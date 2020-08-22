from page.base_page import BasePage

#流量上网页面
class RoamingPage(BasePage):
    def exchange_one(self):
        return self.step('../steps/roaming_page.yaml', 'exchange_one')

    def buy_by_alipay(self):
        return self.step('../steps/roaming_page.yaml', 'buy_by_alipay')

    def buy_by_wechat(self):
        return self.step('../steps/roaming_page.yaml', 'buy_by_wechat')

    def help(self):
        return self.step('../steps/roaming_page.yaml', 'help')