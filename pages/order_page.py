from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class OrderPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME  = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS    = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO      = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE      = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON= (By.XPATH, "//button[normalize-space()='Далее']")

    DATE           = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN  = (By.XPATH, "//div[contains(@class,'Dropdown-control')]")
    def RENT_OPTION(self, text):
        return (By.XPATH, f"//div[contains(@class,'Dropdown-menu')]//div[normalize-space()='{text}']")
    COLOR_BLACK    = (By.ID, "black")
    COLOR_GREY     = (By.ID, "grey")
    COMMENT        = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON   = (By.XPATH, "//div[contains(@class,'Order_Content') or contains(@class,'Order_NextButton')]/descendant::button[normalize-space()='Заказать' and not(@disabled)]")

    CONFIRM_MODAL  = (By.XPATH, "//div[contains(@class,'Modal') and .//div[contains(text(),'Хотите оформить заказ?')]]")
    CONFIRM_YES    = (By.XPATH, "//div[contains(@class,'Modal')]//button[normalize-space()='Да']")
    SUCCESS_MODAL  = (By.XPATH, "//div[contains(@class,'Modal') and .//*[contains(text(),'Заказ') and (contains(text(),'оформлен') or contains(text(),'создан'))]]")

    def fill_step1(self, first, last, address, metro, phone):
        self.find(self.FIRST_NAME).send_keys(first)
        self.find(self.LAST_NAME).send_keys(last)
        self.find(self.ADDRESS).send_keys(address)
        metro_input = self.find(self.METRO)
        metro_input.clear()
        metro_input.send_keys(metro)
        metro_input.send_keys(Keys.DOWN, Keys.ENTER)
        self.find(self.PHONE).send_keys(phone)
        self.click(self.NEXT_BUTTON)

    def fill_step2(self, date_str, rent_text, color='black', comment=''):
        date_input = self.find(self.DATE)
        date_input.click()
        date_input.clear()
        date_input.send_keys(date_str)
        date_input.send_keys(Keys.ENTER)
        self.click(self.RENT_DROPDOWN)
        self.click(self.RENT_OPTION(rent_text))
        if color == 'black':
            self.click(self.COLOR_BLACK)
        elif color == 'grey':
            self.click(self.COLOR_GREY)
        if comment:
            self.find(self.COMMENT).send_keys(comment)

    def submit_and_confirm(self):
        self.click(self.ORDER_BUTTON)
        self.find_visible(self.CONFIRM_MODAL)
        self.click(self.CONFIRM_YES)

    def wait_success(self):
        self.find_visible(self.SUCCESS_MODAL)
        return True

