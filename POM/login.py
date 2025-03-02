import time

from _library.Selenium_wrapper import SeleniumWrapper
from data.excel_read import login_locator

locator = login_locator()


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.seleniumwrapper = SeleniumWrapper(self.driver)

    def enter_email(self, email):
        self.seleniumwrapper.wait_till_ele_visible(locator['login_id'])
        self.seleniumwrapper.enter_data(locator['login_id'], email)

    def enter_pwd(self, pwd):
        self.seleniumwrapper.wait_till_ele_visible(locator['login_pwd'])
        self.seleniumwrapper.enter_data(locator['login_pwd'], pwd)

    def login_btn(self):
        self.seleniumwrapper.wait_till_ele_visible(locator['login_btn'])
        self.seleniumwrapper.clk_on_ele(locator['login_btn'])
        time.sleep(4)







