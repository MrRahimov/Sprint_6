def test_open_main(driver):
    driver.get("https://qa-scooter.praktikum-services.ru/")
    assert "qa-scooter" in driver.current_url

