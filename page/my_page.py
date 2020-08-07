from page.balancemore_page import BalanceMorePage
from page.base_page import BasePage
from page.feedback_page import FeedbackPage
from page.pointsmore_page import PointsMorePage
from page.realname_page import RealNamePage


#我的页面
from page.version_page import VersionPage


class MyPage(BasePage):
    def my_orders(self):
        return self.step('../steps/my_page.yaml', 'my_orders')

    def recommend(self):
        return self.step('../steps/my_page.yaml', 'recommend')

    def my_points(self):
        self.step('../steps/my_page.yaml', 'my_points')
        return PointsMorePage(self.driver)

    def my_balance(self):
        self.step('../steps/my_page.yaml', 'my_balance')
        return BalanceMorePage(self.driver)

    def goto_pointsFragment(self):
        self.step('../steps/my_page.yaml', 'my_points')
        from page.points_page import PointsPage
        return PointsPage(self.driver)

    def goto_realname(self):
        self.step('../steps/my_page.yaml', 'goto_realname')
        return RealNamePage(self.driver)

    def goto_feedback(self):
        self.step('../steps/my_page.yaml', 'goto_feedback')
        return FeedbackPage(self.driver)

    def goto_help(self):
        return self.step('../steps/my_page.yaml', 'goto_help')

    def goto_version(self):
        self.step('../steps/my_page.yaml', 'goto_version')
        return VersionPage(self.driver)
