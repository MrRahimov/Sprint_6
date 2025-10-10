import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    opts = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=opts)  # без менеджеров драйверов
    driver.maximize_window()
    yield driver
    driver.quit()

