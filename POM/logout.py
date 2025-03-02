import time

from POM.login import Login
from _library.Selenium_wrapper import SeleniumWrapper
from data.excel_read import logout_locator

locator = logout_locator()


class Logout(Login):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.seleniumwrapper = SeleniumWrapper(self.driver)

    def clk_ham_btn(self):
        self.seleniumwrapper.wait_till_ele_visible(locator['hamburger_btn'])
        self.seleniumwrapper.clk_on_ele(locator['hamburger_btn'])

    def clk_logout(self):
        self.seleniumwrapper.wait_till_ele_visible(locator['logout_btn'])
        self.seleniumwrapper.clk_on_ele(locator['logout_btn'])
        time.sleep(2)

