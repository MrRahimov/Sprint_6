from pages.main_page import MainPage

def test_open_main(driver):
    main = MainPage(driver)
    main.open_main()
    assert "qa-scooter" in main.current_url()
