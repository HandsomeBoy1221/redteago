from page.base_page import BasePage

#钻石详细列表页面
class BalanceMorePage(BasePage):
    def get_first_record(self):
        return self.step('../steps/balancemore_page.yaml', 'get_first_record')