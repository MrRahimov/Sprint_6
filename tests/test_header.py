from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage

def test_logo_scooter_leads_home(driver):
    main = MainPage(driver)
    main.open_main()
    main.click_order_bottom()
    main.click_scooter_logo()
    assert "qa-scooter" in driver.current_url

def test_logo_yandex_opens_dzen_in_new_tab(driver):
    main = MainPage(driver)
    main.open_main()
    prev_tabs = driver.window_handles
    main.click_yandex_logo()
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > len(prev_tabs))
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 15).until(lambda d: d.current_url.lower() != "about:blank")
    url = driver.current_url.lower()
    assert ("dzen" in url) or ("ya.ru" in url) or ("yandex" in url), f"Ожидали Дзен/Яндекс, получили: {url}"

