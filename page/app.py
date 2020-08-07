from appium import webdriver

from page.base_page import BasePage
from page.login_page import LoginPage

#App启动页，包含APP启动参数，重启，停止，跳转至登录页
class App(BasePage):
    def start(self):
        if self.driver==None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '10'
            desired_caps['deviceName'] = '7ef6e589'
            desired_caps['appPackage'] = 'com.redteamobile.domestic.redteago'
            desired_caps['appActivity'] = 'com.redteamobile.ferrari.ui.splash.SplashActivity'
            desired_caps['noReset'] = False  # 不清除缓存
            #desired_caps['skipDeviceInitialization'] = True  # 跳过安装，权限设置等操作
            desired_caps['unicodeKeyBoard'] = True
            desired_caps['resetKeyBoard'] = True
            desired_caps['autoGrantPermissions'] = True
            desired_caps['automationName'] = 'uiautomator2'
            desired_caps['newCommandTimeout']= 120
            #desired_caps['dontStopAppOnReset'] = True
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(5)
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        # self.driver.launch_app()
        # self.driver.implicitly_wait(5)
        self.driver.start_activity('com.redteamobile.domestic.redteago','com.redteamobile.ferrari.ui.splash.SplashActivity')
        self.driver.implicitly_wait(5)

    def goto_login(self):
        return LoginPage(self.driver)