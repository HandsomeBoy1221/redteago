from page.base_page import BasePage


#意见反馈页面
class FeedbackPage(BasePage):
    def send_question(self,question):
        self._params['question'] = question
        self.step('../steps/feedback_page.yaml', 'send_question')
        return self

    def send_phone(self,phone):
        self._params['phone'] = phone
        self.step('../steps/feedback_page.yaml', 'send_phone')
        return self

    def send_qq(self,qq):
        self._params['qq'] = qq
        self.step('../steps/feedback_page.yaml', 'send_qq')
        return self

    def send(self):
        self.step('../steps/feedback_page.yaml', 'send')
        return self