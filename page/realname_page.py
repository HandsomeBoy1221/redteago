from page.base_page import BasePage

#实名认证页面
class RealNamePage(BasePage):
    def get_text(self):
        return self.step('../steps/realname_page.yaml', 'get_text')