import pytest
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_argument('--disable-notifications')
opts.add_experimental_option('detach', True)


@pytest.fixture()
def _driver():
    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()



