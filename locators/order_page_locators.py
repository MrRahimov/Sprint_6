from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME  = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS    = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO      = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE      = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON= (By.XPATH, "//button[normalize-space()='Далее']")

    DATE           = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN  = (By.XPATH, "//div[contains(@class,'Dropdown-control')]")
    @staticmethod
    def RENT_OPTION(text: str):
        return (By.XPATH, f"//div[contains(@class,'Dropdown-menu')]//div[normalize-space()='{text}']")

    COLOR_BLACK    = (By.ID, "black")
    COLOR_GREY     = (By.ID, "grey")
    COMMENT        = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON   = (By.XPATH, "//div[contains(@class,'Order_Content') or contains(@class,'Order_NextButton')]/descendant::button[normalize-space()='Заказать' and not(@disabled)]")

    CONFIRM_MODAL  = (By.XPATH, "//div[contains(@class,'Modal') and .//div[contains(text(),'Хотите оформить заказ?')]]")
    CONFIRM_YES    = (By.XPATH, "//div[contains(@class,'Modal')]//button[normalize-space()='Да']")
    SUCCESS_MODAL  = (By.XPATH, "//div[contains(@class,'Modal') and .//*[contains(text(),'Заказ') and (contains(text(),'оформлен') or contains(text(),'создан'))]]")
