import re
import sys

import allure

print(sys.path.append('..'))


import pytest
import yaml

from page.app import App

with open('../datas/test_runall.yaml',encoding='utf-8') as f:
    read=yaml.safe_load(f)['test_read']
with open('../datas/test_runall.yaml',encoding='utf-8') as f:
    game=yaml.safe_load(f)['test_game']

class TestRunAll():
    #启动APP
    @allure.story('初始化APP')
    def setup_class(self):
        self.app=App()
        with allure.step('登录'):
            #13524031864
            self.main=self.app.start().goto_login().send_phone('13524031864').send_code()

    #关闭APP
    @allure.story('关闭APP')
    def teardown_class(self):
        self.app.stop()

    #执行完用例后回到首页，保证用例之间的独立性
    @allure.story('重启APP')
    def teardown(self):
        self.app.restart()

    #检查操作指引文案
    @allure.story('操作指引')
    @pytest.mark.skip
    def test_help1(self):
        with allure.step('检查操作指引文案'):
            text = self.main.goto_roaming().help()
            assert '具体' in text

    #检测兑换功能
    @allure.story('兑换套餐')
    def test_exchange(self):
        with allure.step('进入体验-1小时400M流量包套餐详情页'):
            more=self.main.goto_roaming()
        with allure.step('兑换套餐'):
            text=more.exchange_one()
        with allure.step('检查订单页是否有可启用套餐'):
            assert '启用' in text

    #检测购买功能-支付宝
    @allure.story('购买套餐-支付宝')
    def test_buy1(self):
        with allure.step('进入联通-24小时2GB-高速流量套餐详情页'):
            more=self.main.goto_roaming()
        with allure.step('购买套餐-支付宝'):
            text=more.buy_by_alipay()
        with allure.step('检查是否跳转至支付宝支付页'):
            assert '使用支付密码登录' in text

    #检测购买功能-微信
    @allure.story('购买套餐-微信')
    def test_buy2(self):
        with allure.step('进入联通-24小时2GB-高速流量套餐详情页'):
            more=self.main.goto_roaming()
        with allure.step('购买套餐-微信'):
            text=more.buy_by_wechat()
        with allure.step('检查是否跳转至微信支付页'):
            assert '微信号/QQ/邮箱登录' in text

    #检查好友推荐
    @allure.story('领取金币->好友推荐')
    def test_recommend1(self):
        with allure.step('查看推荐好友'):
            text=self.main.goto_pointsFragment().recommend()
        with allure.step('检查推荐列表是否有推荐人'):
            assert '****' in text


    #检查签到功能
    @allure.story('签到')
    def test_registration(self):
        with allure.step('点击签到'):
            registration=self.main.goto_pointsFragment().registration()
        with allure.step('判断是否签到成功'):
            assert '已签到' in registration

    #检查创意广告1
    @allure.story('创意视频I')
    def test_Reward1(self):
        with allure.step('点击观看广告'):
            open=self.main.goto_pointsFragment().Reward1()
        with allure.step('查看金币列表第一条记录'):
            first_record=open.goto_my().my_points().get_first_record()
        with allure.step('判断金币数额是否为70'):
            num = re.sub("\D", "", first_record)
            assert int(num) == 70

    #检查创意广告2
    @allure.story('创意视频II')
    def test_Reward2(self):
        with allure.step('点击观看广告'):
            open=self.main.goto_pointsFragment().Reward2()
        with allure.step('查看金币列表第一条记录'):
            first_record = open.goto_my().my_points().get_first_record()
        with allure.step('判断金币数额是否为70'):
            num = re.sub("\D", "", first_record)
            assert int(num) == 70

    #检查创意广告3
    @allure.story('创意视频III')
    def test_Reward3(self):
        with allure.step('点击观看广告'):
            open=self.main.goto_pointsFragment().Reward3()
        with allure.step('查看金币列表第一条记录'):
            first_record = open.goto_my().my_points().get_first_record()
        with allure.step('判断金币数额是否为70'):
            num = re.sub("\D", "", first_record)
            assert int(num) == 70


    #遍历阅读列表中的跳转，并断言金币是否增加
    @allure.story('阅读')
    @pytest.mark.parametrize('read_name,points',read)
    def test_read(self,read_name,points):
        with allure.step('进入阅读'):
            read_one=self.main.goto_pointsFragment().read().read_one(read_name)
        with allure.step('金币是否增加'):
            num=str(read_one).split(' ')[2].split('/')[0]
            assert int(num)>points

    #遍历游戏列表中的跳转，并断言金币是否增加
    @allure.story('游戏')
    @pytest.mark.parametrize('game_name,points',game)
    def test_game(self,game_name,points):
        with allure.step('进入游戏'):
            game_one=self.main.goto_pointsFragment().game().game_one(game_name)
        with allure.step('金币是否增加'):
            num = str(game_one).split(' ')[2].split('/')[0]
            assert int(num)>points

    #检查跳转功能，并断言金币是否增加
    @allure.story('跳转')
    @pytest.mark.skip
    def test_dump(self):
        with allure.step('点击跳转'):
            dump=self.main.goto_pointsFragment().dump()
        with allure.step('查看金币列表第一条记录'):
            first_record =dump.goto_my().my_points().get_first_record()
        with allure.step('判断增加金币是否为11'):
            num = re.sub("\D", "", first_record)
            assert int(num) == 11

    #检查全部订单-开启/关闭套餐
    @allure.story('全部订单-开启/关闭套餐')
    def test_orders(self):
        with allure.step('进入全部订单页'):
            orders=self.main.goto_my().my_orders()
        with allure.step('开启订单'):
            text=orders.open_orders()
        with allure.step('检查套餐是否开启'):
            assert '暂停' in text
        with allure.step('关闭订单'):
            text=orders.close_orders()
        with allure.step('检查套餐是否关闭'):
            assert '启用' in text

    #检查分享好友页面跳转
    @allure.story('我的->好友推荐')
    def test_recommend2(self):
        with allure.step('查看推荐好友'):
            text=self.main.goto_my().recommend()
        with allure.step('检查推荐列表是否有推荐人'):
            assert '****' in text

    # 检查金币钻石解释文案
    @allure.story('什么是金币、钻石')
    def test_pointstip(self):
        with allure.step('点击进入金币钻石解释页面'):
            text=self.main.goto_my().points_tip()
        with allure.step('检查文案是否正确'):
            assert '您获取的钻石在3天' in text


    #检查钻石列表是否为空
    @allure.story('我的钻石')
    def test_balance(self):
        with allure.step('获取钻石列表'):
            first_record=self.main.goto_my().my_balance().get_first_record()
        with allure.step('钻石列表不为空'):
            assert '钻石' in first_record

    #检查实名认证页面文案显示
    @allure.story('实名认证')
    def test_realname(self):
        with allure.step('检查页面文案'):
            text=self.main.goto_my().goto_realname().get_text()
            assert '身份证正面' in text

    #检查帮助中心文案显示
    @allure.story('帮助中心')
    def test_help2(self):
        with allure.step('检查帮助中心文案'):
            text=self.main.goto_my().goto_help()
            assert '订单中看不到怎么办' in text

    #检查意见反馈功能是否正常
    @allure.story('意见反馈')
    def test_feedback(self):
        with allure.step('填写信息并提交'):
            self.main.goto_my().goto_feedback().send_question('test').send_phone('17312345678').send_qq('691234567').send()

    @allure.story('版本信息')
    def test_protocol(self):
        with allure.step('服务协议'):
            text=self.main.goto_my().goto_version().protocol()
            assert '多多流量宝' in text


    @allure.story('版本信息')
    def test_policy(self):
        with allure.step('隐私政策'):
            text=self.main.goto_my().goto_version().policy()
            assert '更新日期' in text
