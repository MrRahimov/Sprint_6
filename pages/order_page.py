from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as L


class OrderPage(BasePage):
    def fill_step1(self, first, last, address, metro, phone):
        self.find(L.FIRST_NAME).send_keys(first)
        self.find(L.LAST_NAME).send_keys(last)
        self.find(L.ADDRESS).send_keys(address)

        metro_input = self.find(L.METRO)
        metro_input.clear()
        metro_input.send_keys(metro)
        metro_input.send_keys(Keys.DOWN, Keys.ENTER)

        self.find(L.PHONE).send_keys(phone)
        self.click(L.NEXT_BUTTON)

    def fill_step2(self, date_str, rent_text, color='black', comment=''):
        date_input = self.find(L.DATE)
        date_input.click()
        date_input.clear()
        date_input.send_keys(date_str)
        date_input.send_keys(Keys.ENTER)

        self.click(L.RENT_DROPDOWN)
        self.click(L.RENT_OPTION(rent_text))

        self.click((By.ID, color))

        if comment:
            self.find(L.COMMENT).send_keys(comment)

    def submit_and_confirm(self):
        self.click(L.ORDER_BUTTON)
        self.find_visible(L.CONFIRM_MODAL)
        self.click(L.CONFIRM_YES)

    def wait_success(self):
        self.find_visible(L.SUCCESS_MODAL)
        return True
