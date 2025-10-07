from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

DEFAULT_TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, url: str):
        self.driver.get(url)

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, locator) -> str:
        return self.find_visible(locator).text

    def scroll_into_view(self, locator):
        el = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        return el

