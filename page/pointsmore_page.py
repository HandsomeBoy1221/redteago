from page.base_page import BasePage


#金币列表详情页
class PointsMorePage(BasePage):
    def get_first_record(self):
        return self.step('../steps/pointsmore_page.yaml', 'get_first_record')