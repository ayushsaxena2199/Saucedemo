from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumWrapper:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def clk_on_ele(self, logical_name):
        self.driver.find_element(*logical_name).click()

    def enter_data(self, logical_name, data):
        self.driver.find_element(*logical_name).send_keys(data)

    def scroll_to_ele(self, logical_name):
        ele = self.driver.find_element(*logical_name)
        ac_obj = ActionChains(self.driver)
        ac_obj.scroll_to_element(ele).perform()

    def wait_till_ele_visible(self, logical_name):
        ele = self.driver.find_element(*logical_name)
        wait_obj = WebDriverWait(self.driver, 10)
        wait_obj.until(ec.visibility_of(ele))

    def clear_textfield(self, logical_name):
        self.driver.find_element(*logical_name).clear()



