from pages.base_page import BasePage
from data.urls import BASE_URL
from locators.main_page_locators import MainPageLocators as L

class MainPage(BasePage):
    URL = BASE_URL

    def open_main(self):
        self.open(self.URL)

    def click_order_top(self):
        self.scroll_into_view(L.ORDER_BUTTON_TOP)
        self.click(L.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.scroll_into_view(L.ORDER_BUTTON_BOTTOM)
        self.click(L.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click(L.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(L.YANDEX_LOGO)
