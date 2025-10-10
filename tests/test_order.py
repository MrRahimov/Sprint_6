import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import order_data

@pytest.mark.parametrize("data", order_data)
def test_positive_order_flow_from_top(driver, data):
    main = MainPage(driver)
    order = OrderPage(driver)
    main.open_main()
    main.click_order_top()
    order.fill_step1(data["first"], data["last"], data["address"], data["metro"], data["phone"])
    order.fill_step2(data["date"], data["rent"], color=data["color"], comment=data["comment"])
    order.submit_and_confirm()
    assert order.wait_success()

@pytest.mark.parametrize("data", order_data)
def test_positive_order_flow_from_bottom(driver, data):
    main = MainPage(driver)
    order = OrderPage(driver)
    main.open_main()
    main.click_order_bottom()
    order.fill_step1(data["first"], data["last"], data["address"], data["metro"], data["phone"])
    order.fill_step2(data["date"], data["rent"], color=data["color"], comment=data["comment"])
    order.submit_and_confirm()
    assert order.wait_success()
