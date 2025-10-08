from pages.main_page import MainPage

def test_logo_scooter_leads_home(driver):
    main = MainPage(driver)
    main.open_main()
    main.click_order_bottom()
    main.click_scooter_logo()
    assert "qa-scooter" in main.current_url()

def test_logo_yandex_opens_dzen_in_new_tab(driver):
    main = MainPage(driver)
    main.open_main()
    before = len(main.window_handles())
    main.click_yandex_logo()
    main.wait_tabs_more_than(before, timeout=10)
    last = main.window_handles()[-1]
    main.switch_to_window(last)
    main.wait_url_not("about:blank", timeout=15)
    url = main.current_url().lower()
    assert ("dzen" in url) or ("ya.ru" in url) or ("yandex" in url)
