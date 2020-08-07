import time

from page.base_page import BasePage
from page.roaming_page import RoamingPage
from page.my_page import MyPage
from page.points_page import PointsPage

#首页
class MainPage(BasePage):
    def goto_pointsFragment(self):
        self.step('../steps/main_page.yaml', 'goto_pointsFragment')
        return PointsPage(self.driver)

    def goto_my(self):
        self.step('../steps/main_page.yaml', 'goto_my')
        return MyPage(self.driver)

    def goto_roaming(self):
        self.step('../steps/main_page.yaml', 'goto_roaming')
        return RoamingPage(self.driver)