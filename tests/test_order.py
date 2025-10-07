import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

order_data = [
    {
        "first": "Иван",
        "last": "Иванов",
        "address": "г. Москва, Тестовая 1",
        "metro": "Черкизовская",
        "phone": "+79990000001",
        "date": "10.10.2025",
        "rent": "трое суток",
        "color": "black",
        "comment": "Позвоните за 10 минут"
    },
    {
        "first": "Петр",
        "last": "Петров",
        "address": "г. Москва, Примерная 2",
        "metro": "Сокольники",
        "phone": "+79990000002",
        "date": "11.10.2025",
        "rent": "сутки",
        "color": "grey",
        "comment": "Код домофона 1234"
    },
]

entry_points = ["top", "bottom"]

@pytest.mark.parametrize("entry", entry_points)
@pytest.mark.parametrize("data", order_data)
def test_positive_order_flow(driver, entry, data):
    main = MainPage(driver)
    order = OrderPage(driver)

    main.open_main()
    if entry == "top":
        main.click_order_top()
    else:
        main.click_order_bottom()

    order.fill_step1(
        data["first"], data["last"], data["address"], data["metro"], data["phone"]
    )
    order.fill_step2(
        data["date"], data["rent"], color=data["color"], comment=data["comment"]
    )
    order.submit_and_confirm()
    assert order.wait_success(), "Не появилось окно об успешном создании заказа"

