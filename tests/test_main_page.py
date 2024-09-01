import random

import allure
from allure_commons.types import Severity

from pages.main_page import MainPage
from pages.user_page import UserPage
from faker import Faker


@allure.title("Checking the elements presence on main page")
@allure.severity(severity_level=Severity.MINOR)
def test_elements_on_main_page(browser, base_url):
    with allure.step("Open URL"):
        browser.get(base_url)
    main_page = MainPage(browser)
    with allure.step("Check elements on the page"):
        main_page.check_elements_on_main_page()


@allure.title("Checking the user's ability to sign in")
@allure.severity(severity_level=Severity.BLOCKER)
def test_user_registration(browser, base_url):
    fake = Faker()
    with allure.step("Open URL"):
        browser.get(base_url)
    main_page = MainPage(browser)
    with allure.step("Go to registration page"):
        main_page.go_to_registration_page()
    user_page = UserPage(browser)
    name = fake.first_name()
    lastname = fake.last_name()
    password = f'{name[:5].replace(' ', '')}{lastname[:5].replace(' ', '')}{random.randrange(100, 999)}'
    with allure.step(
        "Complete registration and make sure the new user actually exists"
    ):
        user_page.registration(name, lastname, password)
    user_page.check_registration_success()
    print("Message for allure report")


@allure.title("Checking the user's ability to switch the currency")
@allure.severity(severity_level=Severity.NORMAL)
def test_switch_currency(browser, base_url):
    with allure.step("Open URL"):
        browser.get(base_url)
    main_page = MainPage(browser)
    product_name, product_price = main_page.get_feature_products_name_price()

    with allure.step("Switching the currency"):
        main_page.switch_currency()
    product_name_2, product_price_2 = main_page.get_feature_products_name_price()

    with allure.step(
        "Make sure the exact products price is now present in different currency"
    ):
        assert product_name == product_name_2 and product_price != product_price_2
