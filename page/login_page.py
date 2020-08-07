from page.base_page import BasePage
from page.main_page import MainPage


#登录页面
class LoginPage(BasePage):

    def send_phone(self,phone):
        self._params['phone'] = phone
        self.step('../steps/login_page.yaml', 'send_phone')
        return self

    def send_code(self):
        self.step('../steps/login_page.yaml', 'send_code')
        return MainPage(self.driver)