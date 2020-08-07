from page.base_page import BasePage


#游戏列表页面
class GameMorePage(BasePage):
    def game_one(self,game_name):
        self._params['game_name']=game_name
        return self.step('../steps/gamemore_page.yaml', 'game_one')