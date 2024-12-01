import random

import allure
import pytest
from allure_commons.types import Severity

from pages.main_page import MainPage
from pages.product_page import ProductPage
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

@allure.title("Checking the user's ability to add a few products to the cart")
@allure.severity(severity_level=Severity.NORMAL)
@pytest.mark.parametrize("number", [1, 5, 20], ids=['one item', 'a few items', 'many items'])
def test_put_item_in_shopping_cart(browser, base_url, number):
    with allure.step("Open URL"):
        browser.get(base_url)
    main_page = MainPage(browser)
    product_page = ProductPage(browser)
    product_name, product_price = main_page.get_feature_products_name_price()

    with allure.step("Go to products page"):
        main_page.click_featured_product()

    with allure.step(f"Add item to cart {number} times"):
        product_page.click_add_to_cart(number)

    with allure.step('Go to cart page'):
        main_page.go_to_cart_page()

    with allure.step('Get products name and price in cart'):
        product_cart_name, product_cart_price = main_page.get_shopping_cart_product_name()

    with allure.step(f'Assert the price is correct to the amount ({number}) of {product_name}'):
        assert product_price*number == product_cart_price, (f'The price in the cart "{product_cart_price}" doesn\'t '
                                                            f'equal the price in card - "{product_price}"')


@allure.title("Checking the user's ability to add a few products to the cart")
@allure.severity(severity_level=Severity.NORMAL)
@pytest.mark.parametrize("number", [1, 3], ids=['one item', 'three items'])
def test_delete_item_from_shopping_cart(browser, base_url, number):
    with allure.step("Open URL"):
        browser.get(base_url)
    main_page = MainPage(browser)
    product_page = ProductPage(browser)

    with allure.step("Go to products page"):
        main_page.click_featured_product()

    with allure.step(f"Add item to cart {number} times"):
        product_page.click_add_to_cart(number)

    with allure.step('Go to cart page'):
        main_page.go_to_cart_page()

    with allure.step(f'Delete the product added'):
        main_page.delete_item_added_to_cart()




