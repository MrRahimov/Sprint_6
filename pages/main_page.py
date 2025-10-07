from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.urls import BASE_URL

class MainPage(BasePage):
    URL = BASE_URL

    ORDER_BUTTON_TOP = (By.XPATH, "//button[normalize-space()='Заказать' and not(@id)][1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[normalize-space()='Заказать' and not(@id)])[last()]")

    SCOOTER_LOGO = (By.XPATH, "//img[contains(@alt,'Scooter') or contains(@alt,'Самокат')]/ancestor::a")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")

    def open_main(self):
        self.open(self.URL)

    def click_order_top(self):
        self.scroll_into_view(self.ORDER_BUTTON_TOP)
        self.click(self.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.scroll_into_view(self.ORDER_BUTTON_BOTTOM)
        self.click(self.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

