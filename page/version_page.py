from page.base_page import BasePage


class VersionPage(BasePage):
    def protocol(self):
        return self.step('../steps/version_page.yaml', 'protocol')

    def policy(self):
        return self.step('../steps/version_page.yaml', 'policy')