from page.base_page import BasePage

#版本信息页面
class VersionPage(BasePage):
    def protocol(self):
        return self.step('../steps/version_page.yaml', 'protocol')

    def policy(self):
        return self.step('../steps/version_page.yaml', 'policy')