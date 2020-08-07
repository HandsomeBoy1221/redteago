import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.gamemore_page import GameMorePage
from page.readmore_page import ReadMorePage


#领取金币页面
class PointsPage(BasePage):

    status = (By.ID, 'com.redteamobile.domestic.redteago:id/btnRegistration')


    def registration(self):
        if '已签到' in self.find(self.status).text:
            return '已签到'
        else:
            return self.step('../steps/points_page.yaml', 'registration')


    def Reward1(self):
        self.step('../steps/points_page.yaml', 'Reward1')
        return self

    def Reward2(self):
        self.step('../steps/points_page.yaml', 'Reward2')
        return self

    def read(self):
        self.step('../steps/points_page.yaml', 'read')
        return ReadMorePage(self.driver)

    def game(self):
        self.step('../steps/points_page.yaml', 'game')
        return GameMorePage(self.driver)

    def dump(self):
        self.step('../steps/points_page.yaml', 'dump')
        return self

    def goto_my(self):
        self.step('../steps/points_page.yaml', 'goto_my')
        from page.my_page import MyPage
        return MyPage(self.driver)

    def recommend(self):
        return self.step('../steps/points_page.yaml', 'recommend')