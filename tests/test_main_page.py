from pages.main_page import MainPage
from pages.user_page import UserPage


def test_elements_on_main_page(browser, base_url):
    browser.get(base_url)
    main_page = MainPage(browser)
    main_page.check_elements_on_main_page()


def test_user_registration(browser, base_url):
    browser.get(base_url)
    main_page = MainPage(browser)
    main_page.go_to_registration_page()
    user_page = UserPage(browser)
    user_page.registration('Jack', 'Peterson', 'JacPete24')
    user_page.check_registration_success()


def test_switch_currency(browser, base_url):
    browser.get(base_url)
    main_page = MainPage(browser)
    product_name, product_price = main_page.get_feature_products_name_price()
    main_page.switch_currency()
    product_name_2, product_price_2 = main_page.get_feature_products_name_price()
    assert product_name == product_name_2 and product_price != product_price_2
