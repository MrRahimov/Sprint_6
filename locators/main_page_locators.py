from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[normalize-space()='Заказать' and not(@id)][1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[normalize-space()='Заказать' and not(@id)])[last()]")
    SCOOTER_LOGO = (By.XPATH, "//img[contains(@alt,'Scooter') or contains(@alt,'Самокат')]/ancestor::a")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
