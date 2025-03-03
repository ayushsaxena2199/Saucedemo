import pytest
from selenium import webdriver


@pytest.fixture(params=["Chrome", "Edge"])
def _driver(request):
    if request.param == "Chrome":
        opts = webdriver.ChromeOptions()
        opts.add_argument('--disable-notifications')
        opts.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=opts)
    elif request.param == "Edge":
        opts = webdriver.EdgeOptions()
        opts.add_argument('--disable-notifications')
        driver = webdriver.Edge(options=opts)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()



