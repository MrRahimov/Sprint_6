from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from data.urls import BASE_URL

class FaqPage(BasePage):
    URL = BASE_URL

    def question(self, i: int):
        return (By.ID, f"accordion__heading-{i}")

    def answer(self, i: int):
        return (By.ID, f"accordion__panel-{i}")

    def open_main(self):
        self.open(self.URL)

    def expand_question(self, i: int):
        self.scroll_into_view(self.question(i))
        self.click(self.question(i))
        panel = self.find(self.answer(i))
        WebDriverWait(self.driver, 10).until(lambda d: panel.text.strip() != "")
        return panel

    def get_answer_text(self, i: int) -> str:
        return self.get_text(self.answer(i)).strip()

